from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializer
from rest_framework import status


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
