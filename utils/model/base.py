from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True
