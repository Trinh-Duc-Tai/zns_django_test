# Generated by Django 5.0 on 2023-12-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leeon_zns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionLogZN',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('content', models.TextField()),
                ('template_code', models.CharField(max_length=11)),
                ('template_type', models.SmallIntegerField()),
                ('price', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('response_msg_id', models.CharField(max_length=100)),
                ('response_error', models.CharField(max_length=10)),
                ('response_message', models.CharField(max_length=50)),
                ('zalo_sent_time', models.DateTimeField()),
                ('remaining_quota', models.CharField(max_length=50)),
                ('daily_quota', models.CharField(max_length=50)),
                ('sending_mode', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'transaction_log',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TransactionLogZNS',
        ),
    ]