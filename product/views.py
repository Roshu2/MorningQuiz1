from unicodedata import category
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer
from .models import Category, Item, Order, ItemOrder


class ProductView(APIView):
    
    def get(self, request):
        # category = request['category']
        # items = Item.objects.filter(category=category)
        items = Item.objects.all()
        item_serializer = ItemSerializer(items, many=True).data
        
        return Response(item_serializer, status=status.HTTP_200_OK)