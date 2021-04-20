from guias.models import Cliente, DetalleGuia
from principal.models import PaisesList


def create_detalle_envio(**kwargs):
    cliente = Cliente.objects.create(
        nombre=kwargs.get('nombre'),
        apellido=kwargs.get('apellido'),
        email=kwargs.get('email'),
        empresa=kwargs.get('empresa')
    )
    detalle_guia = DetalleGuia.objects.create(
        pais=kwargs.get('pais'),
        direccion=kwargs.get('direccion'),
        direccion_secundaria=kwargs.get('direccion_secundaria'),
        telefono=kwargs.get('telefono'),
        tipo_telefono=kwargs.get('tipo_telefono'),
        codigo_pais=kwargs.get('codigo_pais'),
        cliente=cliente
    )
    return detalle_guia


def update_detalle_envio(detalle_guia, **kwargs):
    detalle_guia.cliente.nombre = kwargs.get('nombre')
    detalle_guia.cliente.apellido = kwargs.get('apellido')
    detalle_guia.cliente.email = kwargs.get('email')
    detalle_guia.cliente.empresa = kwargs.get('empresa')
    detalle_guia.cliente.save()
    detalle_guia.pais = kwargs.get('pais')
    detalle_guia.direccion = kwargs.get('direccion')
    detalle_guia.direccion_secundaria = kwargs.get('direccion_secundaria')
    detalle_guia.telefono = kwargs.get('telefono')
    detalle_guia.tipo_telefono = kwargs.get('tipo_telefono')
    detalle_guia.codigo_pais = kwargs.get('codigo_pais')
    detalle_guia.save()
