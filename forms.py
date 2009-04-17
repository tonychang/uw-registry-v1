from django import forms
from django.forms import ModelForm
from uwregistry.models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['owner', 'date_submitted', 'date_modified', 'status']

    def clean_nickname(self):
        nick = self.cleaned_data['nickname']
        if nick == 'admin' or nick == 'service':
            raise forms.ValidationError("The nickname '%s' is not usable." % nick)
        return nick


class ServiceEditForm(ServiceForm):
    class Meta:
        model = Service
        exclude = ['owner', 'date_submitted', 'date_modified', 'status', 'nickname']

