# Generated by Django 4.2.10 on 2024-02-12 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0003_create_stock_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='merchandise',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='merchandise.merchandise'),
        ),
    ]
