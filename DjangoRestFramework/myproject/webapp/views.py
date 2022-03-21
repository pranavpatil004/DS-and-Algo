from django.shortcuts import render

from django.shortcuts import get_object_or_404
from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import employeeSerializer
from .models import employees

# Create your views here.

class employeeList(APIView):
    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)
    def post(self, request):
        pass
