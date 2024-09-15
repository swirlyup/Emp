from django.urls import path
from .views import UserListCreateView

urlpatterns = [
    #สำหรับดูjsonทั้งหมด
    path("", UserListCreateView.as_view(), name="user_list"),
]