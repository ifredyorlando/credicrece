from allauth.account import app_settings
from allauth.account.forms import ChangePasswordForm
from allauth.exceptions import ImmediateHttpResponse
from allauth.utils import get_form_class
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView
from allauth.account.views import AjaxCapableProcessFormViewMixin, sensitive_post_parameters_m, LoginView

from users.models import Users

# Create your views here.

class LoginCustomView(LoginView):

    def form_valid(self, form):
        success_url = self.get_success_url()
        data = self.request.POST
        user = User.objects.filter(username=data['login']).first()
        if user is not None and not user.is_superuser:
            profile = Users.objects.filter(user_id=user.id).first()
            if profile is not None:
                profile.bloqueo = 0
                profile.save()
                if (timezone.now() - profile.date_change_password).days >= 90:
                    print('Working!!')
                    #return HttpResponseRedirect(reverse_lazy('main:change-password-custom', kwargs={'pk': user.id}))
        try:
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response
