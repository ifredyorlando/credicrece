from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import _password_validators_help_text_html
from django.db import transaction
from django.db.models import Q
from django.utils import timezone


from users.models import User
from utils import FieldModelModalFormMixin


class UserCreateForm(UserCreationForm, forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
        help_text=_password_validators_help_text_html(),
    )
    groups = forms.ModelChoiceField(label='Rol', queryset=Group.objects.all())    

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_active',
            'groups'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if not user.is_superuser and user.groups.all().first().name != 'Administrador':
            self.fields['groups'].queryset = Group.objects.filter(~Q(name='Administrador'))
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class UserUpdateForm(forms.ModelForm):
    groups = forms.ModelChoiceField(label='Rol', queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'groups'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if not user.is_superuser and user.groups.all().first().name != 'Administrador':
            self.fields['groups'].queryset = Group.objects.filter(~Q(name='Administrador'))
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class ChangePasswordUserForm(FieldModelModalFormMixin):
    new_password = forms.CharField(label='Contraseña', strip=False, help_text=_password_validators_help_text_html())

    class Meta:
        model = User
        fields = ['id', 'new_password']

    def clean_new_password(self):
        password = self.cleaned_data.get('new_password')
        password_validation.validate_password(password, self.instance)
        return password

    @transaction.atomic
    def save(self, commit=True):
        password = self.cleaned_data['new_password']
        user = self.instance
        user.set_password(password)
        if commit:
            Perfil.objects.filter(usuario_id=user.id).update(date_change_password=timezone.now())
            user.save()
        return user
