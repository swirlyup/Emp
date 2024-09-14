from django.urls import path
from .views import ListEmp, DetailEmp

urlpatterns = [
    #สำหรับดูjsonทั้งหมด
    path("", ListEmp.as_view(), name="emp_list"),
    #สำหรับ api/emp/<id>
    path("<int:pk>/", DetailEmp.as_view(), name="emp_detail"),
]