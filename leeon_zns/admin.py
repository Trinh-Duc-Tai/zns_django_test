from django.contrib import admin
from .models import TransactionLogZN, Template, Customer
from django.utils.html import format_html
from django.utils.translation import gettext as _
from django.urls import reverse

admin.site.site_title = "ZNS"
admin.site.site_header = "ZNS Administration"
# admin.site.index_title = "ZNS Administration"

class TransactionLogZNSAdmin(admin.ModelAdmin):
    # list_filter = TransactionLogZN.FilterableFields
    search_fields = TransactionLogZN.SearchableFields
    list_display = ('id', 'customer_id', 'content_template', 'template_code', 'template_type', 'price', 'phone_number', 'formatted_created_at', 'tran_id', 'response_message')
    list_display_links = ('content_template',)
    readonly_fields = ('id', 'customer_id', 'content', 'template_code', 'template_type', 'price', 'phone_number', 'response_msg_id', 'response_error', 'response_message', 'zalo_sent_time', 'remaining_quota', 'daily_quota', 'sending_mode', 'transaction_id', 'created_at')
    list_per_page = 5
    # list_display_links = None
    def has_add_permission(self, request):      #hide button Add
        return False
    
    def has_delete_permission(self, request, obj=None):     #hide button Delete
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False  # Ẩn nút "Save"
        extra_context['show_save_and_continue'] = False  # Ẩn nút "Save and continue editing"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def tran_id(self,obj):
        return format_html(f'{obj.transaction_id} ')
    tran_id.short_description = _('tran_id')
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created At')

    def content_template(self,obj):
        return format_html(f'{obj.content[:29]} <span style="color:red"> ... (More)</span>')
    content_template.short_description = _('Content')

admin.site.register(TransactionLogZN, TransactionLogZNSAdmin)

class TemplateAdmin(admin.ModelAdmin):
    # list_display = Template.DisplayFields
    search_fields = ('template_name', 'created_at')
    list_display = ("template_name", "content_template" ,"template_code" ,"type", "price", "formatted_created_at","view")
    list_display_links = ('content_template',)
    # def view(self,obj):
    #     return format_html('<i class="fa-regular fa-eye" style="color:#ff6b6b; font-size:15px; cursor: pointer"></i>')
    def view(self, obj):
        view_url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id])
        # return format_html(f'<a href="javascript:void(0);" class="view-link" data-url="{view_url}"><i class="fa-regular fa-eye" style="color:#ff6b6b; font-size:15px; cursor: pointer"></i></a>')
        return format_html(f'<a href="" class="view-link" data-url="{view_url}"><i class="fa-regular fa-eye" style="color:#ff6b6b; font-size:15px; cursor: pointer"></i></a>')
    view.short_description = 'View'

    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'leeon_zns/js/admin_custom.js',)

    def formatted_created_at(self, obj):
        formatted_datetime = (obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created At')

    def content_template(self,obj):
        return format_html(f'{obj.content[:29]} <span style="color:red"> ... (More)</span>')
    content_template.short_description = _('Content')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # extra_context['show_save'] = False  # Ẩn nút "Save"
        # extra_context['show_save_and_continue'] = False  # Ẩn nút "Save and continue editing"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    # def has_view_permission(self, request, obj=None):
    #     return request.user.has_perm('leeon_zns.view_template')

admin.site.register(Template, TemplateAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'balance_limit', 'balance_current', 'ip_limit', 'token', 'email', 'phone_number', 'formatted_created_at')
    search_fields = Customer.SearchableFields
    list_per_page = 3
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Created At')
    
admin.site.register(Customer, CustomerAdmin)