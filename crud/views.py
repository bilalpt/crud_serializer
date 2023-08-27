from django.shortcuts import render
from .serializers import StudentsSerializer
from .models import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def StudentDetails(request,id):
    std=Student.objects.get(id=id)
    print(std)
    serializer=StudentsSerializer(std)
    print(serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)

    return HttpResponse(json_data, content_type='application/json')
