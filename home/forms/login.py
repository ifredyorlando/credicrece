from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from users.models import Users


class FormLoginCustom(LoginForm):

    def clean(self):
        data = self.data
        if data is not None:
            user = User.objects.filter(username=data['login']).first()
            if user is not None and not user.is_superuser:
                profile = Users.objects.filter(user_id=user.id).first()
                if profile is not None and profile.bloqueo >= 3:
                    raise forms.ValidationError('Usuario bloqueado por 3 o más intentos fallidos al iniciar sesión'
                                                ' contacte a su administrador')
        return super(FormLoginCustom, self).clean()

    def __init__(self, *args, **kwargs):
        data = kwargs.get('data')
        super(FormLoginCustom, self).__init__(*args, **kwargs)
        if data is not None:
            user = User.objects.filter(username=data['login']).first()
            if user is not None and not user.is_superuser and not check_password(data['password'], user.password):
                profile = Users.objects.filter(user_id=user.id).first()
                if profile is not None:
                    profile.bloqueo += 1
                    profile.save()
