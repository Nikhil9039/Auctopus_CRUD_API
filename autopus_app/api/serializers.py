from autopus_app.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
 class Meta:
  model = Product
  fields = ['id', 'tittle', 'warnty', 'created_on', 'price', 'desc']
  
