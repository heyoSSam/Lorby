from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view()
def register(request):
    if request.method == 'GET':
        posts = User.objects.all()
        serializer = UserSerializer(posts, many=True)
        return Response({"data": serializer.data})

    elif request.method == 'POST':
        user = request.data
        user_sql = User(login=user.login, password = user.password, email = user.email)
        user_sql.save()
