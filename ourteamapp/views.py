from django.shortcuts import render
from .models import ourteampage
from .serialziers import OurTeamSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser


class OurTeamList(APIView):
   
    def get(self, request,  *args, **kwargs):
        snippets = ourteampage.objects.all()
        serializer = OurTeamSerializer()
        return render(request,'ourteamapp/ourteam.html')

    def post(self, request,  *args, **kwargs):
        #if request.user.is_superuser:
            serializer = OurTeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return render('ourteam-form')
            return render(request,'ourteamapp/ourteam.html')

class OurTeamDetail(APIView):
   

    def get(self, request,*args, **kwargs):
        snippets = ourteampage.objects.all()
        serializer = OurTeamSerializer()
        return render(request,'ourteamapp/ourteamfoam.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            snippets =  ourteampage.objects.all()
            serializer = OurTeamSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('ourteam-form')
            return render('/failed/')
               
   # def delete(self, request, slug, format=None):
    #    if request.user.is_superuser:
     #       snippet = self.get_object(slug)
     #       snippet.delete()
      #      return Response(status=status.HTTP_204_NO_CONTENT)












# Create your views here.
# def ourteam(request):
#     ourteamview = ourteampage.objects.all()
#     return render(request, 'ourteamapp/ourteam.html' , {'ourteamview':ourteamview})


#class OurTeam(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = OurTeamSerializer
#    queryset = ourteampage.objects.all()
