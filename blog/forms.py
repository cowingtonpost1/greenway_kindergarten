import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import CATEGORIES
from .models import Project


class new_project_form(forms.ModelForm):
    # key = forms.CharField(widget=forms.TextInput())
    class Meta():
        model = Project
        exclude = ['id']
