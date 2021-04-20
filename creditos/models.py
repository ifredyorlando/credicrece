from django.db import models

# Create your models here.
from utils.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _
import random
from clientes.models import Cliente
import uuid

class Credito(BaseModel):
    PLAZOS = (
        ('diario','Diario'),
        ('semanal','Semanal'),
        ('quincenal','Quincenal'),
        ('mensual','Mensual'),
    )
    cliente_asignado = models.ForeignKey(
        Cliente,
        on_delete = models.CASCADE,
        verbose_name = 'Credito a nombre de '
    )

    monto = models.FloatField(_('Monto'))
    plazo = models.CharField(_('Plazo'),max_length=25,choices=PLAZOS,default='diario')
    forma_de_pago = models.CharField(_('Forma de pago'),max_length=25)
    taza_de_interes = models.FloatField(_('Taza de interes'),default=15)
    tipo_garantia = models.CharField(_('Tipo de garantia'),max_length=50)
    desembolsado = models.BooleanField(_('Credito desembolsado'),default=False)
    pagado = models.BooleanField(_('Credito pagado'),default=False)
    

    #Descripcion de garantiaa

    descripcion_garantia = models.CharField(_('Descripcion de la garantia'),max_length=25)
    marca = models.CharField(_('Marca'),max_length=25)
    numero_serie = models.CharField(_('Numero de serie'),max_length=25)
    modelo = models.CharField(_('Modelo'),max_length=50)
    cic = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    imagen = models.ImageField(upload_to ='uploads/')

    cuota_capital = models.FloatField(_('Cuota capital'),default=0)
    cuota_interes = models.FloatField(_('Cuota de interes'),default=0)
    cuota_total = models.FloatField(_('Cuota total'),default=0)
    cuotas_pendientes = models.FloatField(_('Cantidad de cuotas pendientes'),default=0)
    cuota_total_diaria = models.FloatField(_('Cuota total diaria'),default=0)
    cuota_interes_diaria = models.FloatField(_('Cuota de interes diaria'),default=0)

