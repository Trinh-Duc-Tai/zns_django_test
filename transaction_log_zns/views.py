from django.shortcuts import render
from django.http import HttpResponse
from .models import TransactionLogZNS
from django.db import connection

def template_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT template_name, created_at FROM template")
        templates = cursor.fetchall()
    return render(request, 'transaction_log_zns/template_list.html', {'templates': templates})

def transaction_log_list(request):
    transaction_log_list = TransactionLogZNS.objects.order_by("-created_at")[:5]
    context = {'transaction_log_list': transaction_log_list}
    return render(request, 'transaction_log_zns/transaction_log_list.html', context)

def hi(request):
    return HttpResponse("<h1>Subscribe to DevPanda</h1>")