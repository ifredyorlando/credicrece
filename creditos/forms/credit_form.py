from django import forms
from ..models import Credito
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
class CreditoForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cliente_asignado',css_class='form-group col-md-6 mb-0'),
                Column('monto',css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('plazo',css_class='form-group col-md-6 mb-0'),
                Column('forma_de_pago',css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('taza_de_interes',css_class='form-group col-md-6 mb-0'),
                Column('tipo_garantia',css_class='form-group col-md-6 mb-0')
            ),
            Div(                                                                     
            Row(
                Column(HTML('<h4 class="title">Descripcion de garantia</h4>'),css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column(HTML('<hr/>'),css_class='form-group col-md-12 mb-0')
            ),
            ),
            Row(
                Column('descripcion_garantia',css_class='form-group col-md-6 mb-0'),
                Column('marca',css_class='form-group col-md-6 ,b-0')
            ),
            Row(
                Column('numero_serie',css_class='form-group col-md-6 mb-0'),
                Column('modelo',css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('imagen',css_class='form-group col-md-6 mb-0'),
                
            )

        )
    class Meta:
        model = Credito
        fields =  ('cliente_asignado', 'monto', 'plazo','forma_de_pago','taza_de_interes',
    'tipo_garantia','tipo_garantia','descripcion_garantia','marca','numero_serie','modelo','imagen'
    )