from autopus_app.models import Product
from autopus_app.api.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
 queryset = Product.objects.all()
 serializer_class = ProductSerializer
#  authentication_classes = [SessionAuthentication]
#  permission_classes = [IsAuthenticatedOrReadOnly]