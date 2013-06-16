from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.utils import simplejson
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime

from beautifulhue.api import Bridge


def main_page(request):
    
    output = '''
        <html>
            <head><title>%s</title></head>
            <body>
                <h1>%s</h1><p>%s</p>
            </body>
        </html>
    ''' % (
           'Django Bookmarks', 
           'Welcome to Django Bookmarks', 
           'Where you can store and share bookmarks!'
    )
    template = 'main.html'
    return render(request, template, content_type="text/html")
    #return HttpResponse(output)