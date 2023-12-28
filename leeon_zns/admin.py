from django.contrib import admin
from .models import TransactionLogZN, Template, Customer
from django.utils.html import format_html
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe
# from googletrans import Translator
# translator = Translator()

admin.site.site_title = "ZNS"
admin.site.site_header = "ZNS Administration"
admin.site.index_title = "ZNS Administration"

class TransactionLogZNSAdmin(admin.ModelAdmin):
    # list_filter = TransactionLogZN.FilterableFields
    search_fields = TransactionLogZN.SearchableFields
    list_display = ('id', 'customer_name', 'content_template', 'template_code', 'template_type', 'price', 'phone_number', 'formatted_created_at', 'response_message')
    list_display_links = ('content_template',)
    readonly_fields = ('id', 'customer_name', 'content', 'template_code', 'template_type', 'price', 'phone_number', 'response_msg_id', 'response_error', 'response_message', 'zalo_sent_time', 'remaining_quota', 'daily_quota', 'sending_mode', 'transaction_id', 'created_at')
    list_per_page = 5
    ordering = ["id"]
    # list_display_links = None
    def has_add_permission(self, request):      #hide button Add
        return False
    
    def has_delete_permission(self, request, obj=None):     #hide button Delete
        return False

    def customer_name(self, obj):
        if obj.customer_id:
            customer = Customer.objects.get(pk=obj.customer_id)
            return customer.customer_name
        return None
    customer_name.short_description = _('Tên khách hàng')
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False  # Ẩn nút "Save"
        extra_context['show_save_and_continue'] = False  # Ẩn nút "Save and continue editing"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    # def tran_id(self,obj):
    #     return format_html(f'{obj.transaction_id} ')
    # tran_id.short_description = _('tran_id')
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Thời gian tạo')
    def content_template(self,obj):
        return format_html(f'{obj.content[:90]} <span style="color:red"> ... (More)</span>')
    content_template.short_description = _('Nội dung mẫu tin')
    def translated_response_message(self, obj):
        # if obj.response_message:
        #     translated_message = translator.translate(obj.response_message, dest='vi').text
        #     return translated_message
        # return None
        return obj.response_message


admin.site.register(TransactionLogZN, TransactionLogZNSAdmin)

class TemplateAdmin(admin.ModelAdmin):
    # list_display = Template.DisplayFields
    search_fields = ('template_name', 'created_at')
    list_display = ('id',"template_name", "content_template" ,"template_code" ,"type", "price", "formatted_created_at")
    list_display_links = ('content_template',)
    ordering = ["id"]

    def view(self,obj):
        return format_html('<i class="fa-regular fa-eye"></i>')
    view.short_description = 'Xem'

    
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Thời gian tạo')

    def content_template(self,obj):
        max_length = 130
        content = obj.content
        if len(content) > max_length:
            content = content[:max_length] + '<span style="color:red"> ... (More)</span>'
        return mark_safe(content)
    content_template.short_description = _('Nội dung mẫu tin')

    def has_delete_permission(self, request, obj=None):     #hide button Delete
        return False

    

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # extra_context['show_save'] = False  # Ẩn nút "Save"
        # extra_context['show_save_and_continue'] = False  # Ẩn nút "Save and continue editing"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    # def has_view_permission(self, request, obj=None):
    #     return request.user.has_perm('leeon_zns.view_template')

admin.site.register(Template, TemplateAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name', 'balance_limit', 'balance_current', 'ip_limit', 'token', 'email', 'phone_number', 'formatted_created_at')
    search_fields = Customer.SearchableFields
    list_per_page = 3
    ordering = ["id"]
    def formatted_created_at(self, obj):
        formatted_datetime = (obj.created_at).strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime
    formatted_created_at.short_description = _('Thời gian tạo')

    def has_delete_permission(self, request, obj=None):     #hide button Delete
        return False
    
admin.site.register(Customer, CustomerAdmin)