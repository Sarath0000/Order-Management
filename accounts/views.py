from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

@api_view(['POST'])
def register(request): # receive request
    serializer = RegisterSerializer(data=request.data) # json is passed into the serializer, stores the data without saving
    if serializer.is_valid(): # serializer check required fields, prepares validated_data, checks data tpe
        serializer.save() # after save, it calls def create()
        return Response(
            {"message" : "customer registered successfully"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
