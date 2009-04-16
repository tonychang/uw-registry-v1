from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from uwregistry.forms import ServiceForm
from datetime import datetime

def home(request):
    return render_to_response(
            'home.html',
            {},
            RequestContext(request),
            )


def service(request, nick):
    return HttpResponse("Service page: %s" % nick)

@login_required
def submit(request):

    if request.method == 'POST':
        form = ServiceForm(data=request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.owner = request.user
            service.status = service.SUBMIT_STAT
            service.date_submitted = datetime.now()
            service.date_modified = datetime.now()
            service.save()
            return HttpResponseRedirect(service.get_absolute_url())
    else:
        form = ServiceForm()

    return render_to_response(
            "submit.html", 
            {
                'form' : form,
            }, 
            context_instance=RequestContext(request))
