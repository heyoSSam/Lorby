from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import PBKDF2PasswordHasher


def hasher(PBKDF2PasswordHasher):
    iterations = PBKDF2PasswordHasher.iterations * 100
    return iterations
@api_view(['GET', 'POST'])
def register(request):

        if request.method == 'POST':
            user = request.data
            user['password'] = hasher(user['password'])
            user_sql = User(login=user['login'], password = user['password'], email = user['email'])
            user_sql.save()

            return Response({"data" : user})
        
        return Response({"data" : "error"})
