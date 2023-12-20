from django.contrib import admin
from django.db import connection
from .models import TransactionLogZNS, Template
from django.db import models

class TransactionLogZNSAdmin(admin.ModelAdmin):
    list_filter = TransactionLogZNS.FilterableFields
    search_fields = TransactionLogZNS.SearchableFields
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

admin.site.register(TransactionLogZNS, TransactionLogZNSAdmin)

class TemplateAdmin(admin.ModelAdmin):
    list_display = Template.DisplayFields
    # readonly_fields = ('template_name', 'created_at')
    search_fields = ('template_name', 'created_at')

    # def get_queryset(self, request):
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT template_name, created_at FROM template")
    #         templates = cursor.fetchall()
    #     return templates
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        # extra_context['show_save'] = False  # Ẩn nút "Save"
        # extra_context['show_save_and_continue'] = False  # Ẩn nút "Save and continue editing"
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

# class TemplateAdmin(admin.ModelAdmin):
#     # list_display = ('template_name', 'created_at')
#     search_fields = ('template_name',)  # Có thể thêm các trường tìm kiếm khác nếu cần

# Đăng ký admin class cho templates
admin.site.register(Template, TemplateAdmin)
