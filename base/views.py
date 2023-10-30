from base.serializers import *
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def index(req):
    return Response(ProductSerializer(Product.objects.all(), many=True).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getImage(req):
    images = []
    products = Product.objects.all()
    for image in products:
        images.append(image.image)
    serializer = ImageSerializer(products, many=True)
    return Response(serializer.data)

