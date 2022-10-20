from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class PersonAPI(APIView):
    def get(self, request, pk= None, format= None):
        id = pk
        if id is not None:
            per = Person.objects.get(id= id)
            serializer = PersonSerializer(per)
            return Response(serializer.data)
        per = Person.objects.all()
        serializer = PersonSerializer(per, many= True)
        return Response(serializer.data)        

    def post(self, request, format= None):
        serializer = PersonSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk, format= None):
        id = pk
        per = Person.objects.get(pk = id)
        serializer = PersonSerializer(per, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'}, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format= None):
        id = pk
        per = Person.objects.get(pk = id)
        serializer = PersonSerializer(per, data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(sel, request, pk, format= None):
        id = pk
        per = Person.objects.get(pk= id)
        per.delete()
        return Response({'msg':'data deleted'})




