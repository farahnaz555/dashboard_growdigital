from django.shortcuts import render
from .models import priceandpackagesmodel
from .serializers import PriceAndPackageSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser


class PriceAndPackagesList(APIView):
    parser_classes = (MultiPartParser,FormParser)

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = priceandpackagesmodel.objects.all()
        serializer = PriceAndPackageSerializer( snippets , many=True )
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_superuser:
            serializer = PriceAndPackageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceAndPackagesDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return priceandpackagesmodel.objects.get(slug=slug)
        except priceandpackagesmodel.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = PriceAndPackageSerializer(snippet)
            return Response(serializer.data)

    def put(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = PriceAndPackageSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




# # Create your views here.
# def priceandpackages(request):
#     priceandpackagesview = priceandpackagesmodel.objects.all()
#     return render(request, 'priceandpackagesapp/priceandpackages.html' , {'priceandpackagesview':priceandpackagesview})

#class PriceAndPackagesList(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = PriceAndPackageSerializer
#    queryset = priceandpackagesmodel.objects.all()
