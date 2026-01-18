from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdmin


@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdmin])
def create_product(request):
    serializer = ProductSerializer(data=request.data) #passes json to serializer and stores without saving
    if serializer.is_valid(): # checks if fields and datatype matches
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_products(request):
    products = Product.objects.all() # product = is a query set
    serializer = ProductSerializer(products, many=True) # translate django model object(products) to JSON
                                          # passing existing products, many = true means (passing multiple(many) objects)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdmin])
def update_product(request, pk):
    try:
        products = Product.objects.get(pk=pk) # products holds the obj to be updated 
    except Product.DoesNotExist:
        return Response({"error" : "Product Not Found"}, status=404)
    serializer = ProductSerializer(products, data=request.data, partial=True) # products = existing obj that selectedc to update
                                                              # data = is the new updated data sent from postman  that replaces existing obj inside products 
                                                              # partial = only updates the field provided , no nees to type the remaining unchanged ones
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdmin])
def delete_product(request, pk):
    try:
        products = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"erroe" : "Product Not Found"}, status=400)
    products.delete()
    return Response({"Message" : "Product Deleted"})    
    









