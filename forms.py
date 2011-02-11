from django import forms
from django.forms import ModelForm
from uwregistry.models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['owner', 'date_submitted', 'date_modified', 'status', 'notes','user_voice_categories']

    def clean(self):
        def data_missing(name):
            return (not name in self.cleaned_data or len(self.cleaned_data[name]) == 0)        

        if not self.cleaned_data['in_development'] and (data_missing('root_url') or data_missing('doc_url')):
            raise forms.ValidationError("Services that are in production must include a service url and doc url.")

        return self.cleaned_data

    def clean_nickname(self):
        nick = self.cleaned_data['nickname']
        if nick == 'admin' or nick == 'service':
            raise forms.ValidationError("The nickname '%s' is not usable." % nick)
        return nick

class ServiceEditForm(ServiceForm):
    class Meta:
        model = Service
        exclude = ['owner', 'date_submitted', 'date_modified', 'status', 'nickname', 'user_voice_categories']
