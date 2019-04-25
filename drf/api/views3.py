from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)