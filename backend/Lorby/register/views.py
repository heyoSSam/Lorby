from django.shortcuts import render

import bcrypt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['GET', 'POST'])
def register(request):

        if request.method == 'POST':
            user = request.data
            print(user)
            serializer = UserSerializer(user)
            print(serializer.data)
            password = str.encode(user['password'])
            salt = bcrypt.gensalt()
            user['password'] = bcrypt.hashpw(password, salt)
            user_sql = User(login=user['login'], password = user['password'], email = user['email'])
            user_sql.save()

            return Response({"data" : user})
        
        return Response({"data" : "error"})
