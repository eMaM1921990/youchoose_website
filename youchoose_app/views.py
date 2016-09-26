from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext


def home(request):
    context = {}
    template = 'index.html'
    return render_to_response(template, context, context_instance=RequestContext(request))
