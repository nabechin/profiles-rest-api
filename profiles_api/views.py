from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializer
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters


class HelloApiView(APIView):
    serializer_class = serializer.HelloSerializer
    def get(self,request,format=None):
        an_apiview = [
        'User Http mothod as function(get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over you application logic',
        'Is mapped manually Url',]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = "Hello {}".format(name)
            return Response({'message':massage})
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        return Response({'method':'PUT'})

    def patch(self,request):
        return Response({'method':'PATCH'})

    def delete(self,request):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializer.HelloSerializer
    def list(self,request):
        a_viewset = [
        'User Action (list,create retrieve,update,partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        serializer = serializer_class(date=request.date)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
