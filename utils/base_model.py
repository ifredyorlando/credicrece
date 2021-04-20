# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
class BaseModel(models.Model):
    """ BaseModel to add general and generic fields to all models"""
    active = models.BooleanField(_('Activo'), default=True)

    class Meta:
        abstract = True
