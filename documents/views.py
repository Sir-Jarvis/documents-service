from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions, status
from .models import *
import json
from django.http import JsonResponse
from .serializers import DocumentSerializer


@permission_classes((permissions.AllowAny,))
class DocumentAPIView(APIView):

    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents,many=True)

        return Response(serializer.data)





@permission_classes((permissions.AllowAny,))
class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request,format=None):
        
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']
        nom = f.name
        typeFile = nom.split(".")[1]

        document, created = Document.objects.get_or_create(document=f,nom=f.name,typeFile=typeFile)
        serializer = DocumentSerializer(document, context={"request": request})

        return Response(serializer.data,status=status.HTTP_201_CREATED)



    



