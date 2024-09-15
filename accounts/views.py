from rest_framework import generics

from .serializers import UserSerializer
from .models import User


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
