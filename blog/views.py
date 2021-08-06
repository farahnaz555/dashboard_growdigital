from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import AllowAny

from rest_framework import generics

from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser

def BlogView(request):
    template_name = "dashboard/blog.html"
    if request.method == "GET":
        items = Blog.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})


def BlogAdd(request):
    template_name = "dashboard/blog.html"
    if request.method == "POST":
        items = BlogModel.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            long_description = request.POST.get('long_description'),
        )
        return redirect('blogview')

def BlogEdit(request,slug):
        template_name = "dashboard/blog.html"
        if request.method == "GET":
            items = BlogModel.objects.get(slug=slug)
            context = {
            'items': items
        }
        return redirect('blogview')
           
        # return render(request, template_name,{"data":context})

    
    

def BlogUpdate(request,slug):
    template_name = "dashboard/blog.html"
    if request.method == "POST":
        items = BlogModel.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            long_description = request.POST.get('long_description'),
        )            
        return redirect('blogview')

        # return render(request, template_name)

    

def BlogDelete(request,slug):
    template_name = "dashboard/blog.html"
    items = BlogModel.objects.get(slug=slug)
    items.delete()
    return redirect('blogview')
   
#class BlogsListView(APIView):
  
 #   def get(self, request, *args, **kwargs):
  #      snippets = Blog.objects.all()
   #     serializer = BlogSerializer()
    #    return render(request,'blog/all_blogs.html')
    #def post(self, request, *args, **kwargs):
        #if request.user.is_superuser:
     #       serializer = BlogSerializer()
      #      if serializer.is_valid():
       #         serializer.save()
        #        return render('blog-form')
         #   return render(request,'blog/all_blogs.html')

#class BlogDetailView(APIView):
  
 #   def get(self, request, *args, **kwargs):
  #      snippets = Blog.objects.all()
   #     serializer = BlogSerializer()
    #    return render(request,'blog/detail.html')

    #   if request.user.is_superuser:
       #     snippets = self.get_object(slug)
        #    serializer = BlogSerializer()
         #   if serializer.is_valid():
          #      serializer.save()
           #     return render('blog-form')
            #return redirect('/failed/')
    
    # return render(request, template_name)

    #def delete(self, request, slug, format=None):
     #   if request.user.is_superuser:
      #      snippet = self.get_object(slug)
       #     snippet.delete()
        #    return Response(status=status.HTTP_204_NO_CONTENT)
        #return Response("Unauthorized Error ", status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)




# def all_blogs(request):
#     blogs = Blog.objects.order_by('-date')
#     return render(request, 'blog/all_blogs.html', {'blogs':blogs})

# def detail(request, blog_id):
#     blog = get_object_or_404(Blog, slug=blog_id)
#     return render(request, 'blog/detail.html',{'blog':blog})

#class BlogsListView(generics.ListAPIView):
#	permission_classes = (AllowAny, )
#	serializer_class = BlogSerializer
#	queryset = Blog.objects.order_by('-date')


#class BlogDetailView(generics.RetrieveAPIView):
#	permission_classes = (AllowAny, )
#	serializer_class = BlogSerializer
#	queryset = Blog.objects.all()
