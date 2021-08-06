from django.shortcuts import render
from .models import portfoliopage
from .serializers import PortfolioSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

#from portfolioapp import views
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser


class PortfolioList(APIView):
   
    def get(self, request,  *args, **kwargs):
        snippets = portfoliopage.objects.all()
        serializer = PortfolioSerializer( snippets , many=True )
        return render(request,'portfolioapp/portfolio.html')

    def post(self, request,  *args, **kwargs):
        if request.user.is_superuser:
            serializer = PortfolioSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PortfolioDetail(APIView):
    

    def get(self, request,  *args, **kwargs):
        snippet = self.get_object(slug)
        serializer = PortfolioSerializer(snippet)
        return Response(serializer.data)

    def put(self, request,  *args, **kwargs):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = PortfolioSerializer(snippet, data=request.data)
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
#def portfolio(request):
   # return(response,'portfolio.html')

#class PortfolioList(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = PortfolioSerializer
#    queryset = portfoliopage.objects.all()
