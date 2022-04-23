from .models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    """
    A simple ViewSet for listing or retrieving users.
    """

    def create(self, *args, **kwargs):
        raise MethodNotAllowed("Not Allowed")

