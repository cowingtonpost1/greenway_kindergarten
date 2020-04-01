import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import CATEGORIES


class new_project_form(forms.Form):
    project_title = forms.CharField(widget=forms.TextInput())
    project_text = forms.CharField(widget=forms.Textarea())
    project_video = forms.CharField(widget=forms.TextInput(), required=False)
    project_category = forms.ChoiceField(choices=CATEGORIES, required=True)
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
