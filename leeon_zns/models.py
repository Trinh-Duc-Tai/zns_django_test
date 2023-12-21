from django.db import models

class TransactionLogZN(models.Model):
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
        verbose_name_plural = 'Log giao dịch'

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
    # DisplayFields = ["template_name", "template_code" ,"type", "price","customer_id", "created_at","updated_at"]
    DisplayFields = ["template_name", "template_code" ,"type", "price", "created_at"]

    class Meta:
        managed = False  # Không quản lý cơ sở dữ liệu
        db_table = 'template'  # Tên bảng trong cơ sở dữ liệu
        verbose_name_plural = 'Các mẫu gửi tin'
        
        # verbose_name = 'Các mẫu'
    def __str__(self):
        return self.template_name +"  |  type: " + str(self.type)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    balance_limit = models.BigIntegerField()
    balance_current = models.BigIntegerField()
    ip_limit = models.CharField(max_length=50)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    SearchableFields = ["customer_name","phone_number", "address", "balance_limit","balance_current", "ip_limit","token"]
    # DisplayFields = ['customer_name', 'balance_limit', 'balance_current', 'ip_limit', 'token', 'updated_at', 'created_at', 'email', 'phone_number', 'address']
    DisplayFields = ['customer_name', 'balance_limit', 'balance_current', 'ip_limit', 'token', 'email', 'phone_number', 'created_at']
    class Meta:
        managed = False
        db_table = 'customer'
        verbose_name_plural = 'Danh sách khách hàng'

    def __str__(self):
        return self.customer_name + "   |   "  + self.ip_limit+ "   |  Limit: " + str(self.balance_limit)+ "   |  Current: " + str(self.balance_current)
