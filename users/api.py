import re
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

    def create(self, *args, **kwargs): # post
        raise MethodNotAllowed("Dead end")

    # def list(self, request):
    #     super().list(request)

    # def retrieve(self, request, pk=None):
    #     super().retrieve(request, pk)

    # def update(self, request, pk=None):
    #     super().update(request, pk)

    # def partial_update(self, request, pk=None):
    #     super().partial_update(request, pk)

    # def destroy(self, request, pk=None):
    #     super().destroy(request, pk)
