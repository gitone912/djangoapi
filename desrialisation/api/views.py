from django.http import HttpResponse
from .serializer import Studentserializers
import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from api import serializer
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method =='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serialiser = Studentserializers(data=pythondata)
        if serialiser.is_valid():
            serialiser.save()
            res ={'msg':'data inserted'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')