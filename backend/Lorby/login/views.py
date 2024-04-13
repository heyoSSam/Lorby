from contextvars import Token

from django.shortcuts import render, get_object_or_404
from djoser.serializers import TokenSerializer, UserSerializer
from requests import Response
from rest_framework import status
from rest_framework.decorators import api_view

from backend.Lorby.register.models import User


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"details": "Not found."}, status=status.HTTP_400_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data})

# @api_view(['GET'])
# # @authentication_classes(Sess)


