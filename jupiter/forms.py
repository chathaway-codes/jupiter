from django import forms
from django.forms import ModelForm
from django.conf import settings

from jupiter.models import Reading

class ReadingForm(ModelForm):
  class Meta:
    model = Reading

