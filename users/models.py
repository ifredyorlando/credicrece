import django
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User,related_name="perfiluser",verbose_name="Usuario",on_delete=models.PROTECT)
    date_change_password = models.DateTimeField(verbose_name="Fecha",default=django.utils.timezone.now)
    is_blocked = models.SmallIntegerField(verbose_name="Bloqueo de cuenta",default=0)

    class Meta:
        app_label = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.user

