# Class Based Views


from .models import Product
from .serializer import ProductSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class ProductList(APIView):
    def get(self,request,*args,**kwargs):
        products = Product.objects.all()
        ser = ProductSerializer(products,many=True)
        return Response(ser.data)
    
    def post(self,request,*args,**kwargs):
        ser = ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateDestroyView(APIView):
    def get(self,request,*args,**kwargs):
        product = Product.objects.get(id=pk)
        ser = ProductSerializer(product)
        return Response(ser.data)
    
    def put(self,request,*args,**kwargs):
        product = Product.objects.get(id=pk)
        ser = ProductSerializer(product,data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data)

    def delete(self,request,*args,**kwargs):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response('Successfully deleted')