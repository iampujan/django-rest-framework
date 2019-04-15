from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def my_product(request):
    
    if request.method == 'GET':
        orm = Product.objects.all()
        ser = ProductSerializer(orm,many=True)
        return Response(ser.data)

    if request.method == 'POST':
        ser = ProductSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data)