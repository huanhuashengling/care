from django.shortcuts import render
from rest_framework.decorators import api_view
from picks.models import Student, Sclass
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json
import webbrowser

# Create your views here. 430921201506070172
@api_view(['GET', 'POST'])
def check(request, format=None):
        # print(request.GET["identity_number"])
    
        identity_number = request.GET["identity_number"]
        student = Student.objects.filter(identity_number=identity_number).first()
        sclass = Sclass.objects.filter(id=student.sclasses_id).first()

        # print(student.student_name)
        class_title = sclass.grade_name + "年级" + sclass.class_name + "班"
        dataset = {"student_name": student.student_name, "class_title": class_title}
        # serializeData = serializers.serialize('json', dataset)
        # print(serializeData)
        url = "http://127.0.0.1:8000/shows/show?identity_number="+identity_number
        webbrowser.open(url)
        return MyJsonResponse(dataset)


class MyJsonResponse(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=False, **kwargs):
        json_dumps_params = dict(ensure_ascii=False)
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)