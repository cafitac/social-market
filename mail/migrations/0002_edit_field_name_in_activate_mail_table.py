# Generated by Django 5.0.2 on 2024-02-07 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_create_activate_mail_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activatemail',
            old_name='is_activated',
            new_name='is_expired',
        ),
    ]
