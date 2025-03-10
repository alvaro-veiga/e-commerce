from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from app.models import *
from app.serializers import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v
        
        return data
    
    @classmethod
    def get__token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['message'] = 'fullstack project'

        return token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    Serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products',
        '/api/products/<id>',
        '/api/users',
        '/api/users/register',
        '/api/users/login',
        '/api/users/profile'
    ]
    return Response(routes)