from django.core.mail import EmailMessage
from urllib.error import HTTPError
import python_http_client
try:
    from ISSE.settings import TEMPLATE_ID_CREACION_GUIA, SENGRID_API_KEY
except ImportError:
    pass


def send_guia_email(email, state='solicitado', guiano=0):
    base_url = 'https://www.isseexpress.com/'
    mail = EmailMessage(
        to=[email]
    )
    mail.content_subtype = 'html'
    mail.body = " "
    # Add template
    mail.template_id = TEMPLATE_ID_CREACION_GUIA
    # Replace substitutions in sendgrid template
    msg = ''
    if state == 'solicitado':
        msg = 'Su paquete ha sido solicidato exitosamente'
    elif state == 'recolectado':
        msg = 'Su paquete ha sido recolectado'
    elif state == 'preparado':
        msg = 'Su paquete esta preparada y listo'
    elif state == 'enviado':
        msg = 'Su paquete esta ruta para ser entragado'
    elif state == 'entregado':
        msg = 'Su paquete esta ruta para ser entragado'
    mail.dynamic_template_data = {
        "msg": msg,
        "guia": guiano
    }
    try:
        mail.send(fail_silently=False)
    except (HTTPError, python_http_client.exceptions.BadRequestsError, python_http_client.exceptions.ForbiddenError) as error:
        print(error)
        print(error.body)
