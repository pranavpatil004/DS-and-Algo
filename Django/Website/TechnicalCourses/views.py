from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    
    return HttpResponse('<h1>Courses</h1>')

def detail(request, course_id):
    return HttpResponse(f'<h1>Course id: {course_id}</h1>')
