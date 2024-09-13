# from django.shortcuts import render
from rest_framework import generics

from .models import Emp
from .serializers import EmpSerializer

"""
CRUD Operation
C = Create
R =Read
U =Update
D =Delete
"""

#for GET/READ API
class ListEmp(generics.ListCreateAPIView):
    queryset = Emp.objects.all().order_by('-id')
    serializer_class = EmpSerializer

#for ดึงID เพื่อ upate หรือ ลบ
class DetailEmp(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all().order_by('-id')
    serializer_class = EmpSerializer