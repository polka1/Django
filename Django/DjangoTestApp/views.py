from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
    text = "IT'S MAIN PAGE"
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)

def basic_one(request):
    view = 'basic_one'
    html = '<html><body>This is %s view</body></html>' % view
    return HttpResponse(html)

def template(request):
    view = "template"
    t = get_template('template.html')
    html = t.render({'name': view})
    return HttpResponse(html)