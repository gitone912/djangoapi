
from functools import partial
import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import student
from .serializer import serializers, studentserializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def studentapi(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = student.objects.get(id=id)
            serializer = studentserializer(stu)
            json_data = JSONRenderer.render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = student.objects.all()
        serializer = studentserializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentserializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data done'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = student.objects.get(id=id)
        serializer = studentserializer(stu,data= pythondata,partial= True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data done'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method =="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = student.objects.get(id = id)
        stu.delete()
        res = {'msg':'data done'}
        json_data= JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')