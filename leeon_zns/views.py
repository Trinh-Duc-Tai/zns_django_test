from django.shortcuts import render
from django.http import HttpResponse
from .models import TransactionLogZN,Customer, Template
from django.db import connection

# def template_list(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT template_name, created_at FROM template")
#         templates = cursor.fetchall()
#     return render(request, 'leeon_zns/template_list.html', {'templates': templates})

def template_list(request):
    templates = Template.objects.order_by("-created_at")[:5]
    context = {'temp_2': templates}
    return render(request, 'leeon_zns/template_list.html', context)

def transaction_log_list(request):
    transaction_log_list = TransactionLogZN.objects.order_by("-created_at")[:5]
    context = {'transaction_log_list': transaction_log_list}
    return render(request, 'leeon_zns/transaction_log_list.html', context)

def customer_list(request):
    customer_list = Customer.objects.order_by("-created_at")[:5]
    context = {'customer_list': customer_list}
    return render(request, 'leeon_zns/customer_list.html', context)

def hi(request):
    return HttpResponse("<h1>Subscribe to DevPanda</h1>")