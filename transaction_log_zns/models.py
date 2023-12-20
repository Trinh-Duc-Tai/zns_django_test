from django.db import models

class TransactionLogZNS(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    content = models.TextField()
    template_code = models.CharField(max_length=11)
    template_type = models.SmallIntegerField()
    price = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    response_msg_id = models.CharField(max_length=100)
    response_error = models.CharField(max_length=10)
    response_message = models.CharField(max_length=50)
    zalo_sent_time = models.DateTimeField()
    remaining_quota = models.CharField(max_length=50)
    daily_quota = models.CharField(max_length=50)
    sending_mode = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    SearchableFields = ["customer_id", "template_code", "phone_number","created_at", "template_type"]
    FilterableFields = ["customer_id", "template_code", "phone_number", "template_type"]

    class Meta:
        managed = False
        db_table = "transaction_log"
        # db_table = "transaction_log_zns"

    def __str__(self):
        return f"Transaction {self.id}"
    
class Template(models.Model):
    id = models.AutoField(primary_key=True)
    template_name = models.TextField()
    template_code = models.CharField(max_length=11)
    content = models.TextField()
    type = models.SmallIntegerField()
    price = models.CharField(max_length=50)
    customer_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    SearchableFields = ["template_name","template_code", "type", "price","customer_id", "created_at","updated_at"]
    DisplayFields = ["template_name", "template_code" ,"type", "price","customer_id", "created_at","updated_at"]

    class Meta:
        managed = False  # Không quản lý cơ sở dữ liệu
        db_table = 'template'  # Tên bảng trong cơ sở dữ liệu
