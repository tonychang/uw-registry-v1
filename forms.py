from django.forms import ModelForm
from uwregistry.models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['owner', 'date_submitted', 'date_modified', 'status']
