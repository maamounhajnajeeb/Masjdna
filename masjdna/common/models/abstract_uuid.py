import uuid

from django.db import models
from django.utils.translation import gettext as _


class AbstractUUIDField(models.Model):
    id = models.UUIDField(
        _("id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True
