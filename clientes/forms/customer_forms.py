from django import forms
from ..models import Cliente 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
              Column('active',css_class='form-group col-md-6 mb-0')  
            ),
            Row(
                Column('primer_nombre',css_class='form-group col-md-6 mb-0'),
                Column('segundo_nombre',css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('tercer_nombre',css_class='form-group col-md-6 mb-0'),
                Column('cuarto_nombre',css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('apellido_de_casada',css_class='form-group col-md-6 mb-0'),
                Column('dpi_cliente',css_class='form-group col-md-6 mb-0')
            ),     
            Row(
                Column('profesion',css_class='form-group col-md-6 mb-0'),
                Column('direccion',css_class='form-group col-md-6 mb-0')
            ), 
            Row(
                Column('telefono_casa',css_class='form-group col-md-6 mb-0'),
                Column('celular',css_class='form-group col-md-6 mb-0')
            ),  
            Row(
                Column('nit',css_class='form-group col-md-6 mb-0'),
                Column('estado_civil',css_class='form-group col-md-6 mb-0')
            ),    
            Row(
                Column('conyugue',css_class='form-group col-md-6 mb-0'),
                Column('condicion_vivienda',css_class='form-group col-md-6 mb-0')
            ),  
            Row(
                Column('correo_electronico',css_class='form-group col-md-6 mb-0'),  
            ),
            Div(                                                                     
            Row(
                Column(HTML('<h4 class="title">Referencias personales</h4>'),css_class='form-group col-md-6 mb-0'),
                Column(HTML('<button onclick=myFunction(personal_references) type="button" class="btn btn-secondary rounded-pill">Cerrar</button>'.format('personal_references')),css_class='form-group col-md-6 mb-0 text-right'),
            ),
            
            Row(
                Column(HTML('<hr/>'),css_class='form-group col-md-12 mb-0')
            ),
            id="header_personal_references"
            ),
            Div(
            Row(
                Column('primera_referencia_p',css_class='form-group col-md-6 mb-0 '),
                Column('segunda_referencia_p',css_class='form-group col-md-6 mb-0 '),
                      
            ),
            Row(
                Column('telefono_primera_referencia_p',css_class='form-group col-md-6 mb-0 '),
                Column('telefono_segunda_referencia_p',css_class='form-group col-md-6 mb-0 ')                
            ),
            id='personal_references'
            ),
            Div(
            Row(
                Column(HTML('<h4 class="title">Referencias Familiares</h4>'),css_class='form-group col-md-6 mb-0'),
                Column(HTML('<button onclick=myFunction(familiar_references) type="button" class="btn btn-secondary rounded-pill">Cerrar</button>'),css_class='form-group col-md-6 mb-0 text-right'),
            ),
            Row(
                Column(HTML('<hr/>'),css_class='form-group col-md-12 mb-0')
            ),
            id="header_familiar_references"
            ),
            Div(
            Row(
                Column('primera_referencia_f',css_class='form-group col-md-6 mb-0'),
                Column('segunda_referencia_f',css_class='form-group col-md-6 mb-0')                
            ),
            Row(
                Column('telefono_primera_referencia_f',css_class='form-group col-md-6 mb-0'),
                Column('telefono_segunda_referencia_f',css_class='form-group col-md-6 mb-0')                
            ),
            id='familiar_references'
            ),
            HTML('<h4 class="title">Personas en relacion de dependencia</h4><hr/>'),
            Row(
                Column('nombre_de_la_empresa_prd',css_class='form-group col-md-6 mb-0'),
                Column('telefono_prd',css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('direccion_de_la_empresa_prd',css_class='form-group col-md-6 mb-0'),
                Column('puesto_de_trabajo_prd',css_class='form-group col-md-6 mb-0'),
            ),            
            Row(
                Column('fecha_inicio_prd',css_class='form-group col-md-6 mb-0'),
                Column('actividad_economica_empresa_prd',css_class='form-group col-md-6 mb-0'),
            ),
            HTML('<h4 class="title">Empresarios/Profesionales</h4><hr/>'),
            Row(
                Column('nombre_de_la_empresa_ep',css_class='form-group col-md-6 mb-0'),
                Column('nit_ep',css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('telefono_ep',css_class='form-group col-md-6 mb-0'),
                Column('fecha_inicio_ep',css_class='form-group col-md-6 mb-0'),
            ),            
        )
    class Meta:
        model = Cliente
        fields = '__all__'