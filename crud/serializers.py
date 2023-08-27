from rest_framework import serializers
from django import forms

class StudentsSerializer(serializers.Serializer):
    name  = serializers.CharField(max_length=200)
    roll  = serializers.IntegerField()
    place = serializers.CharField(max_length=200)

class StudentForm(forms.Form):
    name  = serializers.CharField(max_length=200)
    roll  = serializers.IntegerField()
    place = serializers.CharField(max_length=200)
