from django import forms
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth import get_user_model

from jupiter.models import Reading, PhysicalActivity, Activity

class ReadingForm(ModelForm):
  class Meta:
    model = Reading
    exclude = ('user',)

class UserForm(ModelForm):
  class Meta:
    model = get_user_model()
    exclude = ('password', 'last_login', 'is_superuser',
               'groups', 'user_permissions', 'username',
               'is_staff', 'is_active', 'date_joined',)

class PhysicalActivityForm(ModelForm):
  class Meta:
    model = PhysicalActivity
    exclude = ('user', 'when',)

class ActivityForm(ModelForm):
  class Meta:
    model = Activity
