# Generated by Django 4.2.10 on 2024-02-16 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField()),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order List',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('total_price', models.IntegerField()),
                ('payment_type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_transaction', to='order.order')),
            ],
            options={
                'verbose_name': 'OrderTransaction',
                'verbose_name_plural': 'OrderTransaction List',
                'db_table': 'order_transaction',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('merchandise_id', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItem List',
                'db_table': 'order_item',
            },
        ),
    ]
