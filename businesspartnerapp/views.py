from django.shortcuts import render
from .models import businesspartnerpage
from .serializers import BusinessPartnerSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser


class BusinessPartnerList(APIView):
    
    def get(self, request, *args, **kwargs):
        snippets = businesspartnerpage.objects.all()
        serializer = BusinessPartnerSerializer()
        return render(request,'businesspartnerapp/businesspartner.html')

    def post(self, request, *args, **kwargs):
        #if request.user.is_superuser:
            serializer = BusinessPartnerSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('businesspartner-detail')
            return render(request,'businesspartnerapp/businesspartner.html')
               
class BusinessPartnerDetail(APIView):
   

    def get(self, request, *args, **kwargs):
        snippets = businesspartnerpage.objects.all()
        serializer = BusinessPartnerSerializer()
        return render(request,'businesspartnerapp/businessdetail.html')

    def post(self, request,  *args, **kwargs):
        if request.user.is_superuser:
            snippets = self.get_object(slug)
            serializer = BusinessPartnerSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('businesspartner-detail')
            return redirect('/failed/')

   # def delete(self, request, slug, format=None):
       # if request.user.is_superuser:
         #   snippet = self.get_object(slug)   
          #  snippet.delete()
          #  return Response(status=status.HTTP_204_NO_CONTENT)







# Create your views here.
# def businesspartner(request):
#     businesspartnerview = businesspartnerpage.objects.all()
#     return render(request, 'businesspartnerapp/businesspartner.html' , {'businesspartnerview':businesspartnerview})

#class BusinessPartnerList(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = BusinessPartnerSerializer
#    queryset = businesspartnerpage.objects.all()
