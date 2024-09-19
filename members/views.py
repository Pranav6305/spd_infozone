from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

# members/views.py
from django.http import HttpResponse
from django.template import loader


def home_view(request):
    template = loader.get_template('demo.html')
    return HttpResponse(template.render())

def batch_view(request):
    template = loader.get_template('batch.html')
    return HttpResponse(template.render())

def student_view(request):
    template = loader.get_template('student_detail.html')
    return HttpResponse(template.render())
