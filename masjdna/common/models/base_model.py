from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )

    class Meta:
        abstract = True
