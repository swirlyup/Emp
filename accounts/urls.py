from django.urls import path
from .views import UserListCreateView, UserDetailView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #สำหรับดูjsonทั้งหมด
    path("", UserListCreateView.as_view(), name="user_list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    #jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]