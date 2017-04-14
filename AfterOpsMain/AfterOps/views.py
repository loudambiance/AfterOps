from django.http import HttpResponse
from django.template import loader

def index(request):
    body="Quanticle SUCKS!"
    template =  loader.get_template('index.html')
    context = {
        'body':body,
    }
    return HttpResponse(template.render(context,request))