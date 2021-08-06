from django.shortcuts import render
from .forms import consultationform
from .models import consultationpage
from bizlerapp import views
from .serializers import ConsultationPageSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser


class ConsultionList(APIView):
   
    def get(self, request, *args, **kwargs):
        snippets = consultationpage.objects.all()
        serializer = ConsultationPageSerializer()
        return render(request,'dashboard/consultation.html')

    def post(self, request, *args, **kwargs):
        #if request.user.is_superuser:
            serializer = ConsultationPageSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('consultation-form')
            return render(request,'dashboard/consultation.html')

class ConsultionDetail(APIView):
   
   
    def get(self, request, *args, **kwargs):
        snippets = consultationpage.objects.all()
        serializer = ConsultationPageSerializer()
        return render(request,'dashboard/consultationdetail.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            snippets=self.get_object(slug)
            serializer = ConsultationPageSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('consultion-form')
            return redirect('/failed/')
           

    #def delete(self, request, slug, format=None):
     #   if request.user.is_superuser:
      #      snippet = self.get_object(slug)
       #     snippet.delete()
        #    return Response(status=status.HTTP_204_NO_CONTENT)

#def reviews(request):
#    customerreviewview = customerreviewpage.objects.all()
#    return render(request, 'customerreviewapp/reviews.html', {'customerreviewview':customerreviewview} )

# def consultation(request):
#     if request.method == 'GET':
#         return render(request, 'consultationapp/consultation.html', {'form':consultationform()} )
#     else:
#         try:
#             form = consultationform(request.POST)
#             review = form.save(commit=False)
#             review.save()
#             return redirect('home')
#         except:
#             return render(request, 'consultationapp/consultation.html', {'form':consultationform(), 'error':'Bad data passed in. Try again.'})

#class ConsultionList(generics.ListCreateAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = ConsultationPageSerializer
#    queryset = consultationpage.objects.all()
