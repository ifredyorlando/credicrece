from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import _password_validators_help_text_html
from django.db import transaction
from django.db.models import Q
from django.utils import timezone