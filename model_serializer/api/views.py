import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.parsers import JSONParser
from .models import student
from .serializer import serializers, studentserializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class studentapi(View):
    def get(self,request,*args, **kwargs):
        
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
        
    def post(self,request,*args, **kwargs):
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
    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = studentserializer(data= pythondata,partial= True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data done'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = student.objects.get(id = id)
        stu.delete()
        res = {'msg':'data done'}
        json_data= JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
# Create your views here.
def index(req):
    labels = student.objects.all()
    print(labels)
    chart_data={'a':labels}
    return render(req,'index.html',chart_data)