from django.db import models


class MailHistory(models.Model):

    class Meta:
        db_table = "mail_history"
        verbose_name = "Mail History"
        verbose_name_plural = f"{verbose_name} List"
