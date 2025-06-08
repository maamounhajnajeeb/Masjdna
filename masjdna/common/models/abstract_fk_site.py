from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext as _


class AbstractSiteFK(models.Model):
    site = models.ForeignKey(
        on_delete=models.CASCADE,
        verbose_name=_("related site"),
        to=Site,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
    )

    class Meta:
        abstract = True
