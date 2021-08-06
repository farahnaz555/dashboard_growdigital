from django.shortcuts import render
from .forms import customerreviewform
from .models import customerreviewpage
from .serializers import CustomerReviewSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser

#from rest_framework.permissions import IsAuthenticated


class CustomerReviewList(APIView):
   
    def get(self, request,  *args, **kwargs):
        snippets = customerreviewpage.objects.all()
        serializer = CustomerReviewSerializer()
        return render(request,'customerreviewapp/customerreview.html')

    def post(self, request, *args, **kwargs):
        #if request.user.is_superuser:
            serializer = CustomerReviewSerializer()
            if serializer.is_valid():
                serializer.save()
                return render('customer-form')
            return render(request,'customerreviewapp/customerreview.html')

class CustomerReviewDetail(APIView):
    

    def get(self, request, *args, **kwargs):
        snippet = customerreviewpage.objects.all()
        serializer = CustomerReviewSerializer()
        return render(request,'customerreviewapp/reviews.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            snippet = self.get_object()
            serializer = CustomerReviewSerializer()
            if serializer.is_valid():
                serializer.save()
                return render(request,'customer-form')
            return redirect('/failed/')

    #def delete(self, request, *args, **kwargs):
     #   if request.user.is_superuser:
      #      snippet = self.get_object(slug)
       #     snippet.delete()
        #    return Response(status=status.HTTP_204_NO_CONTENT)


# def reviews(request):
#     customerreviewview = customerreviewpage.objects.all()
#     return render(request, 'customerreviewapp/reviews.html', {'customerreviewview':customerreviewview} )

# def customerreview(request):
#     if request.method == 'GET':
#         return render(request, 'customerreviewapp/customerreview.html', {'form':customerreviewform()} )

#     else:
#         try:
#             form = customerreviewform(request.POST)
#             review = form.save(commit=False)
#             review.save()
#             return redirect('')
#         except:
#             return render(request, 'customerreviewapp/customerreview.html', {'form':customerreviewform(), 'error':'Bad data passed in. Try again.'})

#class CustomerReviewList(generics.ListCreateAPIView):
    #permission_classes = (AllowAny, )
    #serializer_class = CustomerReviewSerializer
    #queryset = customerreviewpage.objects.all()


#def reviews(request):
#    customerreviewview = customerreviewpage.objects.all()
#    return render(request, 'customerreviewapp/reviews.html', {'customerreviewview':customerreviewview} )
