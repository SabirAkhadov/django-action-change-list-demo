from django.contrib import admin
from django.contrib.admin import ModelAdmin, helpers
from django.db.models.aggregates import Count, Sum
from django.utils.encoding import force_text

from .models import SaleSummary, Category


@admin.register(SaleSummary)
class SaleSummaryAdmin(ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'date'

    def changelist_view(self, request, extra_context=None):
        response = super(SaleSummaryAdmin, self).changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        # metrics = {
        #     'total': Count('id'),
        #     'total_sales': Sum('amount'),
        # }
        result_qs = list(qs.values('category__name', 'pk', 'amount').order_by('category__name').all())
        map(lambda r: r.update(
            {'check_box': helpers.checkbox.render(helpers.ACTION_CHECKBOX_NAME, force_text(r['pk']))}), result_qs)
        response.context_data['summary'] = list(result_qs)

        return response


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass
