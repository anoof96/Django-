from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel

# Create your views here.

def home_page(request):
    pass

def student_details(request):
    students_1 = StudentModel.objects.all().filter(standard='1')
    students_2 = StudentModel.objects.all().filter(standard='2')
    students_3 = StudentModel.objects.all().filter(standard='3')
    students_4 = StudentModel.objects.all().filter(standard='4')
    students_5 = StudentModel.objects.all().filter(standard='5')
    students_6 = StudentModel.objects.all().filter(standard='6')
    students_7 = StudentModel.objects.all().filter(standard='7')
    students_8 = StudentModel.objects.all().filter(standard='8')
    students_9 = StudentModel.objects.all().filter(standard='9')
    students_10 = StudentModel.objects.all().filter(standard='10')

    return render(request, 'student_details.html', context={'students_1': students_1, 'students_2': students_2, 'students_3': students_3, 'students_4': students_4, 'students_5': students_5, 'students_6': students_6, 'students_7': students_7, 'students_8': students_8, 'students_9': students_9, 'students_10': students_10})



