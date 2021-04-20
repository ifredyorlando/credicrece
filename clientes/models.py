from django.db import models
from utils.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class Cliente(BaseModel):
    ESTADOS_CIVILES = (('soltero','Soltero'),('casado','Casado'))
    CONDICION_DE_VIVIENDA = (('propia','Propia'),('alquilada','Alquilada'),('usufructo','Usufructo'),('familiar','Familiar'),('adeudada','Adeuda'),('prestada','Prestada'))
    primer_nombre = models.CharField(_('Primer nombre'),max_length=50)
    segundo_nombre = models.CharField(_('Segundo nombre'),max_length=50)
    tercer_nombre = models.CharField(_('Tercer nombre'),max_length=50)
    cuarto_nombre = models.CharField(_('Cuarto nombre'),max_length=50)
    apellido_de_casada = models.CharField(_('Apellido de casada'),max_length=50,null=True,blank=True)
    dpi_cliente = models.CharField(_('DPI'),max_length=50)
    profesion = models.CharField(_('Profesion'),max_length=50)
    direccion = models.CharField(_('Direccion'),max_length=50)
    telefono_casa = models.CharField(_('Telefono de casa'),max_length=50)
    celular = models.CharField(_('Telefono celular'),max_length=50)
    nit = models.CharField(_('Numero de NIT'),max_length=30)
    estado_civil = models.CharField(_('Estado Civil'),max_length = 25,choices=ESTADOS_CIVILES,default='soltero')
    conyugue = models.CharField(_('Conyuge'),max_length=100)
    condicion_vivienda = models.CharField(_('Condicion de vivienda'),max_length = 25, choices = CONDICION_DE_VIVIENDA,default='propia')
    correo_electronico = models.CharField(_('Correo electronico'),max_length = 25)

    #Referencias Personales

    primera_referencia_p = models.CharField(_('Nombre de la Primera referencia'),max_length=50,null=True,blank=True)
    segunda_referencia_p = models.CharField(_('Nombre de la Segunda referencia'),max_length=50,null=True,blank=True)

    telefono_primera_referencia_p = models.CharField(_('Telefono de la Primera referencia'),max_length=50,null=True,blank=True)
    telefono_segunda_referencia_p = models.CharField(_('Telefono de la Segunda referencia'),max_length=50,null=True,blank=True)


    #Referencias Familiares

    primera_referencia_f = models.CharField(_('Nombre Primera Referencia Familiar'),max_length=50,null=True,blank=True)
    segunda_referencia_f = models.CharField(_('Nombre Segunda Referencia Familiar'),max_length=50,null=True,blank=True)

    telefono_primera_referencia_f = models.CharField(_('Telefono de la Primera Referencia Familiar'),max_length=50,null=True,blank=True)
    telefono_segunda_referencia_f = models.CharField(_('Telefono de la Segunda Referencia Familiar'),max_length=50,null=True,blank=True)

    #Personas en relacion de dependencia

    nombre_de_la_empresa_prd = models.CharField(_('Nombre de la empresa'),max_length=50)
    telefono_prd = models.CharField(_('Telefono'),max_length=25)
    direccion_de_la_empresa_prd = models.CharField(_('Direccion de la empresa'),max_length=50)
    puesto_de_trabajo_prd = models.CharField(_('Puesto de trabajo'),max_length = 50)
    fecha_inicio_prd = models.DateField(_('Fecha de inicio'))
    actividad_economica_empresa_prd = models.CharField(_('Actividad economica de la empresa'),max_length=50)

    #Empresarios/Profesionales

    nombre_de_la_empresa_ep = models.CharField(_('Nombre de la empresa'),max_length=50)
    nit_ep = models.CharField(_('NIT'),max_length=25)
    telefono_ep = models.CharField(_('Telefono'),max_length=25)
    fecha_inicio_ep = models.DateField(_('Fecha de inicio'),max_length=25)


    def __str__(self):
        return f'{self.primer_nombre} {self.segundo_nombre} {self.tercer_nombre}'
    