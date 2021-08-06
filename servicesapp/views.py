from django.shortcuts import render
from .models import servicespage
from .serializer import ServicesSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny


from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser


class ServicesList(APIView):
   
    def get(self, request, *args, **kwargs):
        snippets = servicespage.objects.all()
        serializer = ServicesSerializer()
        return render(request,'servicesapp/services.html')

    def post(self, request, *args, **kwargs):
        #if request.user.is_superuser:
            serializer = ServicesSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('service-form')
            return render(request,'servicesapp/services.html')
class ServicesDetail(APIView):
   

    def get(self, request, *args, **kwargs):
        snippets = servicespage.objects.all()
        serializer = ServicesSerializer()
        return render(request,'servicesapp/servicesform.html')

    def put(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = ServicesSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
# def services(request):
#     servicesview = servicespage.objects.all()
#     return render(request, 'servicesapp/services.html' , {'servicesview':servicesview})

#class ServicesList(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = ServicesSerializer
#    queryset = servicespage.objects.all()
