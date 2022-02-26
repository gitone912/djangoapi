from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from api.serializer import StudentSerializer
from .models import Student
# Create your views here.
def student_detail(request):
    stu = Student.objects.get(id = 1)
    serializer= StudentSerializer(stu)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def student_list(request):
    stu = Student.objects.all()
    serializer= StudentSerializer(stu,many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')