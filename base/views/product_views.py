from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from base.products import products 
from base.models import Product
from django.contrib.auth.models import User
from base.serializers import ProductModelSerializer,UserModelSerializer,UserSerializerWithToken




@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializers = ProductModelSerializer(products,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id = pk)
    serializers = ProductModelSerializer(product,many=False)
    return Response(serializers.data)