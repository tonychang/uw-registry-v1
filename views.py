from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return HttpResponse("First home")

def submit(request):
    return render_to_response("submit.html", {})
