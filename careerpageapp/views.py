from django.shortcuts import render
from .models import careerpagepage
from .serializers import CareerPageSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny



from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser


class CareerPageList(APIView):

    def get(self, request, *args, **kwargs):
        snippets = careerpagepage.objects.all()
        serializer = CareerPageSerializer()
        return render(request, 'careerpageapp/careerpage.html')

    def post(self, request, *args, **kwargs):
        # if request.user.is_superuser:
            serializer = CareerPageSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('career-form')
            return render(request, 'careerpageapp/careerpage.html')

class CareerPageDetail(APIView):
        
    def get(self, request, *args, **kwargs):
        snippets=careerpagepage.objects.all()        
        serializer = CareerPageSerializer()
        return render(request, 'careerpageapp/carrerform.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            snippets=careerpagepage.objects.all()        
            serializer = CareerPageSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('career-form')
            return redirect('/failed/')

    # def delete(self, request, slug, format=None):
    #     if request.user.is_superuser:
    #         snippet = self.get_object(slug)
    #         snippet.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
# def careerpage(request):
#     careerpageview = careerpagepage.objects.all()
#     return render(request, 'careerpageapp/careerpage.html' , {'careerpageview':careerpageview})

#class CareerPageList(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = CareerPageSerializer
#    queryset = careerpagepage.objects.all()
