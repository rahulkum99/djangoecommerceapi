from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.products import products 
from . models import Product
from . serializers import ProductModelSerializer
# Create your views here.



@api_view(['GET'])
def getRoutes(request):
    return JsonResponse('hello',safe=False)


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