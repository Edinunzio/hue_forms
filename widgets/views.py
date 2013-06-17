from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.utils import simplejson
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from forms import SigninForm

from datetime import datetime

from beautifulhue.api import Bridge


def main_page(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['username']
            request.session['bridge_ip'] = form.cleaned_data['bridge_ip']
            return dashboard(request)
    template = 'main.html'
    return render(request, template, {'form':form}, content_type="text/html")

def dashboard(request):
    bridge_ip = request.session['bridge_ip']
    username = request.session['username']
    bridge = Bridge(device={'ip':bridge_ip}, user={'name':username})
    resource = {'which':'system'}
    data = bridge.config.get(resource)
        
    template = 'dashboard.html'
    return render(request, template, {'data':data}, content_type="text/html")