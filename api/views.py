from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from rest_framework.views import    APIView

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def addItem(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class UploadFileView(APIView):
    serializer_class = ItemSerializer
    
    def post(self, request):
        request.item = Item.objects.first()
        serializer = self.serializer_class(request.item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    