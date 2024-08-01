# members/views.py
from django.http import HttpResponse
from django.template import loader 

def home_view(request):
    template=loader.get_template('demo.html')
    return HttpResponse(template.render())
