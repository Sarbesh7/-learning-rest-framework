from django.shortcuts import render
from django.http import JsonResponse
from .models import Student

# Create your views here.
def home_api(request):
    return JsonResponse({
        'name': 'sarbesh',
        'age': 20,
        'city': 'butwal'})

def student_list(request):
    students= Student.objects.all()
    student_list = list(students.values())
    return JsonResponse(student_list, safe=False)
    