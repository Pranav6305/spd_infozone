# members/views.py

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Student

def home_view(request):
    return render(request, 'demo.html')

def batch_view(request):
    return render(request, 'batch.html')

def student_list_view(request):
    # Get the filters from the request query parameters
    batch = request.GET.get('batch')
    department = request.GET.get('department')
    rollno = request.GET.get('rollno')

    # Initialize the queryset
    students = Student.objects.all()

    # Apply filters if provided
    if batch:
        students = students.filter(batch=batch)
    if department:
        students = students.filter(department=department)
    if rollno:
        students = students.filter(roll_no=rollno)

    return render(request, 'student_list.html', {'students': students})  

def student_detail_view(request, roll_no):
    student = get_object_or_404(Student, roll_no=roll_no)
    return render(request, 'student_detail.html', {'student': student})     
