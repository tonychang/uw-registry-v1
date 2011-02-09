from django import forms
from django.forms import ModelForm
from django.forms.formsets import BaseFormSet
from django.forms.models import inlineformset_factory,modelformset_factory,BaseModelFormSet,BaseInlineFormSet
from uwregistry.models import Service, ClientLibrary

class ServiceForm(ModelForm):
    root_url_hidden = forms.BooleanField(label='Hide Root URL',
        help_text='Check this if you want your web services hidden to the public')
    class Meta:
        model = Service
        exclude = ['owner', 'date_submitted', 'date_modified', 'status', 'notes']

    def clean_nickname(self):
        nick = self.cleaned_data['nickname']
        if nick == 'admin' or nick == 'service':
            raise forms.ValidationError("The nickname '%s' is not usable." % nick)
        return nick

class ClientLibraryForm(ModelForm):
    class Meta:
        model = ClientLibrary
        exclude = ['id','service']
        


class ServiceEditForm(ServiceForm):
    class Meta:
        model = Service
        exclude = ['owner', 'date_submitted', 'date_modified', 'status', 'nickname']

class BaseServiceClientEditFormSet(BaseInlineFormSet):
#    def __init__(self,**kargs):
#        BaseFormSet.__init__(self,**kargs)
        
    def clean(self):
        print 'test'
    
ServiceClientEditFormSet = inlineformset_factory(Service, ClientLibrary,formset=BaseServiceClientEditFormSet)
#ServiceClientEditFormSet = modelformset_factory(Service)
