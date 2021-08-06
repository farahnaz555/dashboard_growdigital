from django.shortcuts import render
from .models import homepage, aboutuspage, termsncpage, privacypolicypage, sitemappage
from .serializers import *
from bizlerapp import views
from bizlerapp.models import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework.views import APIView,View
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from django.contrib.auth  import authenticate, get_user,  login, logout
from django.contrib import messages

from django.contrib.auth.models import User

# Create your views here.
class Dashboard(View):
    initial = {'key': 'value'}
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name)


class Home(View):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'website/home.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name)

class loginPage(View):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'dashboard/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{"title":"Login"})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # print(user)
        # form = self.form_class(request.POST)
        if user is not None:
            login(request, user)
            # print(get_user(request)) 
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return HttpResponseRedirect('/failed/')



def logoutUser(request):
	logout(request)

	return redirect('login')


class changePassword(View):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'dashboard/change_password.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{"title":"Change Password"})

    def post(self, request, *args, **kwargs):
        # username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(get_user(request))  


        if password2==password1:
            user = authenticate(request, username=get_user(request), password=password)
            # print(user)
            # form = self.form_class(request.POST)
            if user is not None:
                u = User.objects.get(username=get_user(request))
                u.set_password(password1)
                u.save()
                # login(request, user)
                # print(get_user(request)) 
                return redirect('login')
            else:
                messages.info(request, 'Password is incorrect')
                return HttpResponse('/failed due to pass incorrect/')
                # return HttpResponseRedirect('/failed/')
        else:
            messages.info(request, 'Password not matched')
            return HttpResponse('/failed due to pass not match/')
            # return HttpResponseRedirect('/failed/')


# *************************************************************************



# def home(request):
#     homeview = homepage.objects.all()
#     return render(request, 'bizlerapp/home.html', {'homeview':homeview})
# class Home(APIView):
#     parser_classes = (MultiPartParser,FormParser)

#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, *args, **kwargs):
#         snippets = homepage.objects.all()
#         serializer = HomeSerializer()
#         return Response(request, 'home.html')

#     def post(self, request, *args, **kwargs):
#             serializer = HomeSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class HomeDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, slug):
#         try:
#             return homepage.objects.get(slug=slug)
#         except homepage.DoesNotExist:
#             raise Http404

#     def get(self, request, slug, format=None):
#         snippet = self.get_object(slug)
#         serializer = HomeSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, slug, format=None):
#         if request.user.is_superuser:
#             snippet = self.get_object(slug)
#             serializer = HomeSerializer(snippet, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug, format=None):
#         if request.user.is_superuser:
#             snippet = self.get_object(slug)
#             snippet.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#class Home(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = HomeSerializer
#    queryset = homepage.objects.all()

# def aboutus(request):
#     aboutusview = aboutuspage.objects.all()
#     return render(request, 'bizlerapp/aboutus.html', {'aboutusview':aboutusview})

#class AboutUs(generics.ListAPIView):
    #permission_classes = (AllowAny, )
    #serializer_class = AboutUsSerializer
    #queryset = aboutuspage.objects.all()

# ********************** Blog Functions *******************************
def Blogweb(request):
    template_name = "website/blog.html"
    if request.method == "GET":
        items = Blog.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})

def Blogdetail(request):
    template_name = "website/blogdetail.html"
    if request.method == "GET":
        items = Blog.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
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
        items = Blog.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            long_description = request.POST.get('long_description'),
        )
        return redirect('blogview')

        # return render(request, template_name)

def BlogEdit(request,slug):
    template_name = "dashboard/blog.html"
    if request.method == "GET":
        items = Blog.objects.get(slug=slug)
        context = {
            'items': items
        }
        return redirect('blogview')
        # return render(request, template_name,{"data":context})

def BlogUpdate(request,slug):
    template_name = "dashboard/blog.html"
    if request.method == "POST":
        items = Blog.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            long_description = request.POST.get('long_description'),
        )            
        return redirect('blogview')

        # return render(request, template_name)

def BlogDelete(request,slug):
    template_name = "dashboard/blog.html"
    items = Blog.objects.get(slug=slug)
    items.delete()
    return redirect('blogview')
    # return render(request, template_name)


# ********************** Contact Functions *******************************

def Contact(request):
    template_name = "website/contact.html"
    if request.method == "GET":
        items = ContactModel.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})

def ContactInfo(request):
    template_name = "dashboard/contact.html"
    if request.method == "GET":
        items = ContactModel.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})


def ContactAdd(request):
    template_name = "dashboard/contact.html"
    if request.method == "POST":
        items = ContactModel.objects.create(
            title = request.POST.get('title'),
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            # image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            message = request.POST.get('message'),
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # return redirect('contact')


        # return render(request, template_name)

def ContactEdit(request,slug):
    template_name = "dashboard/contact.html"
    if request.method == "GET":
        items = ContactModel.objects.get(slug=slug)
        context = {
            'items': items
        }
        return redirect('contactinfo')
        # return render(request, template_name,{"data":context})

def ContactUpdate(request,slug):
    template_name = "dashboard/contact.html"
    if request.method == "POST":
        items = ContactModel.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            message = request.POST.get('message'),
        )            
        return redirect('contactinfo')

        # return render(request, template_name)

def ContactDelete(request,slug):
    template_name = "dashboard/contact.html"
    items = ContactModel.objects.get(slug=slug)
    items.delete()
    return redirect('contactinfo')
    # return render(request, template_name)

class AboutUs(APIView):
    parser_classes = (MultiPartParser,FormParser)

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = aboutuspage.objects.all()
        serializer = AboutUsSerializer( snippets , many=True )
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_superuser:
            serializer = AboutUsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutUsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return aboutuspage.objects.get(slug=slug)
        except aboutuspage.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = AboutUsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = AboutUsSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# def termsandcondition(request):
#     termsandconditionview = termsncpage.objects.all()
#     return render(request, 'bizlerapp/termsandcondition.html', {'termsandconditionview':termsandconditionview})

class TermsAndCondition(APIView):
    parser_classes = (MultiPartParser,FormParser)


    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = termsncpage.objects.all()
        serializer = TermsSerializer( snippets , many=True )
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_superuser:
            serializer = TermsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TermsAndConditionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return termsncpage.objects.get(slug=slug)
        except termsncpage.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = TermsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = TermsSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        if request.user.is_superuser:
            items = self.get_object(slug)
            items.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

def collabortion(request):
    template_name = "website/collabration.html"
    if request.method == "GET":
        items = consultationpage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def consultationView(request):
    template_name = "dashboard/collabortion.html"
    if request.method == "GET":
         items = consultationpage.objects.all()
         context = {
            'items': items
         }
         return render(request, template_name,{"data":context})


def consultationAdd(request):
    template_name = "dashboard/collabortion.html"
    if request.method == "POST":
       items = consultationpage.objects.create(
            title = request.POST.get('title'),
            # name = request.POST.get('name'),
            message = request.POST.get('message'),
            email = request.POST.get('email'),
            contact = request.POST.get('contact'),
            service = request.POST.get('service'),
        )
    return redirect('collabortioninfo')

        # return render(request, template_name)

def consultationEdit(request,slug):
    template_name = "dashboard/collabortion.html"
    if request.method == "GET":
       items = consultationpage.objects.get(slug=slug)
       context = {
            'items': items
        }
    return redirect('collabortioninfo')
        # return render(request, template_name,{"data":context})

def consultationUpdate(request,slug):
    template_name = "dashboard/collabortion.html"
    if request.method == "POST":
        items = consultationpage.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
           # name = request.POST.get('name'),
            message = request.POST.get('message'),
            email = request.POST.get('email'),
            contact = request.POST.get('contact'),
            service = request.POST.get('service'),
        )            
        return redirect('collabortioninfo')

        # return render(request, template_name)

def consultationDelete(request,slug):
    template_name = "dashboard/collabortion.html"
    items = consultationpage.objects.get(slug=slug)
    items.delete()
    return redirect('collabortioninfo')
    # return render(request, template_name)


#Services model

def service(request):
    template_name = "website/services.html"
    if request.method == "GET":
        items = servicespage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def servicesView(request):
    template_name = "dashboard/services.html"
    if request.method == "GET":
         items = servicespage.objects.all()
         context = {
            'items': items
         }
         return render(request, template_name,{"data":context})


def servicesAdd(request):
    template_name = "dashboard/services.html"
    if request.method == "POST":
       items = servicespage.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
        )
    return redirect('servicesinfo')

        # return render(request, template_name)

def servicesEdit(request,slug):
    template_name = "dashboard/services.html"
    if request.method == "GET":
       items = servicespage.objects.get(slug=slug)
       context = {
            'items': items
        }
    return redirect('servicesinfo')
        # return render(request, template_name,{"data":context})

def servicesUpdate(request,slug):
    template_name = "dashboard/services.html"
    if request.method == "POST":
        items = servicespage.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
        )            
        return redirect('servicesinfo')

        # return render(request, template_name)

def servicesDelete(request,slug):
    template_name = "dashboard/services.html"
    items = consultationpage.objects.get(slug=slug)
    items.delete()
    return redirect('servicesinfo')
    # return render(request, template_name)

#portfolio model

def portfolio(request):
    template_name = "website/portfolio.html"
    if request.method == "GET":
        items = portfoliopage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def portfolioView(request):
    template_name = "dashboard/portfolio.html"
    if request.method == "GET":
         items = portfoliopage.objects.all()
         context = {
            'items': items
         }
         return render(request, template_name,{"data":context})


def portfolioAdd(request):
    template_name = "dashboard/portfolio.html"
    if request.method == "POST":
       items = portfoliopage.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
        )
    return redirect('portfolioinfo')

        # return render(request, template_name)

def portfolioEdit(request,slug):
    template_name = "dashboard/portfolio.html"
    if request.method == "GET":
       items = portfoliopage.objects.get(slug=slug)
       context = {
            'items': items
        }
    return redirect('portfolioinfo')
        # return render(request, template_name,{"data":context})

def portfolioUpdate(request,slug):
    template_name = "dashboard/portfolio.html"
    if request.method == "POST":
        items = portfoliopage.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
        )            
        return redirect('portfolioinfo')

        # return render(request, template_name)

def portfolioDelete(request,slug):
    template_name = "dashboard/portfolio.html"
    items = portfoliopage.objects.get(slug=slug)
    items.delete()
    return redirect('portfolioinfo')
    # return render(request, template_name)

#ourteam model
def Team(request):
    template_name = "website/ourTeam.html"
    if request.method == "GET":
        items = ourteampage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def TeamView(request):
    template_name = "dashboard/ourteam.html"
    if request.method == "GET":
         items = ourteampage.objects.all()
         context = {
            'items': items
         }
         return render(request, template_name,{"data":context})


def TeamAdd(request):
    template_name = "dashboard/ourteam.html"
    if request.method == "POST":
       items = ourteampage.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            designation = request.POST.get('designation'),
            description = request.POST.get('short_description'),
        )
    return redirect('ourteaminfo')

        # return render(request, template_name)

def TeamEdit(request,slug):
    template_name = "dashboard/ourteam.html"
    if request.method == "GET":
       items = ourteampage.objects.get(slug=slug)
       context = {
            'items': items
        }
    return redirect('ourteaminfo')
        # return render(request, template_name,{"data":context})

def TeamUpdate(request,slug):
    template_name = "dashboard/ourteam.html"
    if request.method == "POST":
        items = ourteampage.objects.filter(slug=slug).update(
             title = request.POST.get('title'),
            image = request.FILES.get('image'),
            designation = request.POST.get('designation'),
            description = request.POST.get('short_description'),
        )            
        return redirect('ourteaminfo')

        # return render(request, template_name)

def TeamDelete(request,slug):
    template_name = "dashboard/ourteam.html"
    items = ourteampage.objects.get(slug=slug)
    items.delete()
    return redirect('ourteaminfo')
    # return render(request, template_name)

#career model
def Career(request):
    template_name = "website/career.html"
    if request.method == "GET":
        items = careerpagepage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def CareerView(request):
    template_name = "dashboard/career.html"
    if request.method == "GET":
         items = careerpagepage.objects.all()
         context = {
            'items': items
         }
         return render(request, template_name,{"data":context})


def CareerAdd(request):
    template_name = "dashboard/career.html"
    if request.method == "POST":
       items = careerpagepage.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
        )
    return redirect('careerinfo')

        # return render(request, template_name)

def CareerEdit(request,slug):
    template_name = "dashboard/career.html"
    if request.method == "GET":
       items = careerpagepage.objects.get(slug=slug)
       context = {
            'items': items
        }
    return redirect('careerinfo')
        # return render(request, template_name,{"data":context})

def CareerUpdate(request,slug):
    template_name = "dashboard/career.html"
    if request.method == "POST":
        items = careerpagepage.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
        )            
        return redirect('careerinfo')

        # return render(request, template_name)

def CareerDelete(request,slug):
    template_name = "dashboard/career.html"
    items = careerpagepage.objects.get(slug=slug)
    items.delete()
    return redirect('careerinfo')
    # return render(request, template_name)



#priceandpackage model
def Price(request):
    template_name = "website/pricing.html"
    if request.method == "GET":
        items = priceandpackagesmodel.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def PricePackView(request):
    template_name = "dashboard/pricing.html"
    if request.method == "GET":
         items = priceandpackagesmodel.objects.all()
         context = {
            'items': items
         }
         return render(request, template_name,{"data":context})


def PricePackAdd(request):
    template_name = "dashboard/pricing.html"
    if request.method == "POST":
       items = priceandpackagesmodel.objects.create(
            title = request.POST.get('title'),
            price = request.POST.get('price'),
            description = request.POST.get('description'),
            quantity_purchased = request.POST.get('quantity_purchased'),

        )
    return redirect('pricinginfo')

        # return render(request, template_name)

def PricePackEdit(request,slug):
    template_name = "dashboard/pricing.html"
    if request.method == "GET":
       items = priceandpackagesmodel.objects.get(slug=slug)
       context = {
            'items': items
        }
    return redirect('pricinginfo')
        # return render(request, template_name,{"data":context})

def PricePackUpdate(request,slug):
    template_name = "dashboard/pricing.html"
    if request.method == "POST":
        items = priceandpackagesmodel.objects.filter(slug=slug).update(
           title = request.POST.get('title'),
            price = request.POST.get('price'),
            description = request.POST.get('description'),
            quantity_purchased = request.POST.get('quantity_purchased'),
        )            
        return redirect('pricinginfo')

        # return render(request, template_name)

def PricePackDelete(request,slug):
    template_name = "dashboard/pricing.html"
    items = priceandpackagesmodel.objects.get(slug=slug)
    items.delete()
    return redirect('pricinginfo')
    # return render(request, template_name)
#business mmodel
def businesspartner(request):
    template_name = "website/businesspartner.html"
    if request.method == "GET":
        items = businesspartnerpage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def businesspartnerView(request):
    template_name = "dashboard/businesspartner.html"
    if request.method == "GET":
        items = businesspartnerpage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})


def businesspartnerAdd(request):
    template_name = "dashboard/businesspartner.html"
    if request.method == "POST":
        items = businesspartnerpage.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            long_description = request.POST.get('long_description'),
        )
        return redirect('businesspartnerinfo')

        # return render(request, template_name)

def businesspartnerEdit(request,slug):
    template_name = "dashboard/businesspartner.html"
    if request.method == "GET":
        items = businesspartnerpage.objects.get(slug=slug)
        context = {
            'items': items
        }
        return redirect('businesspartnerinfo')
        # return render(request, template_name,{"data":context})

def businesspartnerUpdate(request,slug):
    template_name = "dashboard/businesspartner.html"
    if request.method == "POST":
        items = businesspartnerpage.objects.filter(slug=slug).update(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            short_description = request.POST.get('short_description'),
            long_description = request.POST.get('long_description'),
        )            
        return redirect('businesspartnerinfo')

        # return render(request, template_name)

def businesspartnerDelete(request,slug):
    template_name = "dashboard/businesspartner.html"
    items = businesspartnerpage.objects.get(slug=slug)
    items.delete()
    return redirect('businesspartnerinfo')
    # return render(request, template_name)


#customerreview mmodel
def customerreview(request):
    template_name = "website/review.html"
    if request.method == "GET":
        items = customerreviewpage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def customerreviewView(request):
    template_name = "dashboard/customerreview.html"
    if request.method == "GET":
        items = customerreviewpage.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})


def customerreviewAdd(request):
    template_name = "dashboard/customerreview.html"
    if request.method == "POST":
        items = customerreviewpage.objects.create(
            name = request.POST.get('name'),
            message  = request.POST.get('message'),
            email = request.POST.get('email'),
        )
        return redirect('customerreviewinfo')

        # return render(request, template_name)

def customerreviewEdit(request,slug):
    template_name = "dashboard/customerreview.html"
    if request.method == "GET":
        items = customerreviewpage.objects.get(slug=slug)
        context = {
            'items': items
        }
        return redirect('customerreviewinfo')
        # return render(request, template_name,{"data":context})

def customerreviewUpdate(request,slug):
    template_name = "dashboard/customerreview.html"
    if request.method == "POST":
        items = customerreviewpage.objects.filter(slug=slug).update(
               name = request.POST.get('name'),
           
            message  = request.POST.get('message'),
            email = request.POST.get('email'),
        )            
        return redirect('customerreviewinfo')

        # return render(request, template_name)

def customerreviewDelete(request,slug):
    template_name = "dashboard/customerreview.html"
    items = customerreviewpage.objects.get(slug=slug)
    items.delete()
    return redirect('customerreviewinfo')
# def privacypolicy(request):
#     privacypolicyview = privacypolicypage.objects.all()
#     return render(request, 'bizlerapp/privacypolicy.html', {'privacypolicyview':privacypolicyview})

# def privacypolicy(request):
#     privacypolicyview = privacypolicypage.objects.all()
#     return render(request, 'bizlerapp/privacypolicy.html', {'privacypolicyview':privacypolicyview})

#class PrivacyPolicy(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = PrivacyPolicySerializer
#    queryset = privacypolicypage.objects.all()

 
#our clientmmodel
def ourClient(request):
    template_name = "website/ourclient.html"
    if request.method == "GET":
        items = ourclient.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})
def ourClientView(request):
    template_name = "dashboard/ourclient.html"
    if request.method == "GET":
        items = ourclient.objects.all()
        context = {
            'items': items
        }
        return render(request, template_name,{"data":context})


def ourClientAdd(request):
    template_name = "dashboard/ourclient.html"
    if request.method == "POST":
        items = ourclient.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            email = request.POST.get('email'),
            contact = request.POST.get('contact'),
            image = request.FILES.get('image'),
        )
        return redirect('ourclientinfo')

        # return render(request, template_name)

def ourClientEdit(request,slug):
    template_name = "dashboard/ourclient.html"
    if request.method == "GET":
        items = ourclient.objects.get(slug=slug)
        context = {
            'items': items
        }
        return redirect('ourclientinfo')
        # return render(request, template_name,{"data":context})

def ourClientUpdate(request,slug):
    template_name = "dashboard/ourclient.html"
    if request.method == "POST":
        items = ourclient.objects.filter(slug=slug).update(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            email = request.POST.get('email'),
            contact = request.POST.get('contact'),
            image = request.FILES.get('image'),
        )            
        return redirect('ourclientinfo')

        # return render(request, template_name)

def ourClientDelete(request,slug):
    template_name = "dashboard/ourclient.html"
    items = ourclient.objects.get(slug=slug)
    items.delete()
    return redirect('ourclientinfo')


class PrivacyPolicy(APIView):
    parser_classes = (MultiPartParser,FormParser)


    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = privacypolicypage.objects.all()
        serializer = PrivacyPolicySerializer( snippets , many=True )
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_superuser:
            serializer = PrivacyPolicySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrivacyPolicyDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return privacypolicypage.objects.get(slug=slug)
        except privacypolicypage.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = PrivacyPolicySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = PrivacyPolicySerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




# def sitemap(request):
#     sitemapview = sitemappage.objects.all()
#     return render(request, 'bizlerapp/sitemap.html', {'sitemapview':sitemapview})

#class SiteMap(generics.ListAPIView):
#    permission_classes = (AllowAny, )
#    serializer_class = SiteMapSerializer
#    queryset = sitemappage.objects.all()



class SiteMap(APIView):
    parser_classes = (MultiPartParser,FormParser)


    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = sitemappage.objects.all()
        serializer = SiteMapSerializer( snippets , many=True )
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_superuser:
            serializer = SiteMapSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiteMapDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return sitemappage.objects.get(slug=slug)
        except sitemappage.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug)
        serializer = SiteMapSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            serializer = SiteMapSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        if request.user.is_superuser:
            snippet = self.get_object(slug)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


def About(request):
    template_name = "website/aboutus.html"
    if request.method == "GET":
        # items = BlogModel.objects.all()
        # context = {
        #     items: items
        # }
        return render(request, template_name)
        # return render(request, template_name,{"data":context})

def TermandCondition(request):
    template_name = "website/termsandcondition.html"
    if request.method == "GET":
        # items = BlogModel.objects.all()
        # context = {
        #     items: items
        # }
        return render(request, template_name)
        # return render(request, template_name,{"data":context})
def PrivacyPolicyView(request):
    template_name = "website/privacypolicy.html"
    if request.method == "GET":
        # items = BlogModel.objects.all()
        # context = {
        #     items: items
        # }
        return render(request, template_name)
        # return render(request, template_name,{"data":context})



def teamdetail(request):
    template_name = "website/ourteamdetail.html"
    #items = Blog.objects.all()
    if request.method == "GET":
        # items = BlogModel.objects.all()
       # context = {
          #  'items': items
      #  }
        return render(request, template_name)
        #return render(request, template_name,{"data":context})