from django.contrib import admin
from .models import TransactionLogZN, Template, Customer
# from django.db import connection

class TransactionLogZNSAdmin(admin.ModelAdmin):
    # list_filter = TransactionLogZN.FilterableFields
    search_fields = TransactionLogZN.SearchableFields
    list_display = ('id', 'customer_id', 'content', 'template_code', 'template_type', 'price', 'phone_number', 'created_at', 'transaction_id', 'response_msg_id', 'response_error', 'response_message', 'zalo_sent_time', 'remaining_quota', 'daily_quota', 'sending_mode')
    readonly_fields = ('id', 'customer_id', 'content', 'template_code', 'template_type', 'price', 'phone_number', 'response_msg_id', 'response_error', 'response_message', 'zalo_sent_time', 'remaining_quota', 'daily_quota', 'sending_mode', 'transaction_id', 'created_at')
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

admin.site.register(TransactionLogZN, TransactionLogZNSAdmin)

class TemplateAdmin(admin.ModelAdmin):
    list_display = Template.DisplayFields
    search_fields = ('template_name', 'created_at')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # extra_context['show_save'] = False  # Ẩn nút "Save"
        # extra_context['show_save_and_continue'] = False  # Ẩn nút "Save and continue editing"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Template, TemplateAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = Customer.DisplayFields
    search_fields = Customer.SearchableFields
    
admin.site.register(Customer, CustomerAdmin)