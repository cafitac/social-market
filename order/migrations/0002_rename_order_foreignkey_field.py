# Generated by Django 4.2.10 on 2024-02-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_create_order_and_order_item_and_order_transaction_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]
