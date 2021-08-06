"""bizler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from bizlerapp import views
#from bizlerapp.views import home , aboutus,privacypolicy, sitemap,termsandcondition
#from myapp.views import index , about,contact,portfolio,services
from django.conf.urls.static import static
from django.conf import settings
#from portfolioapp import views             
from rest_auth.registration.views import VerifyEmailView, RegisterView
from allauth.account.views import ConfirmEmailView
from rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('index/', index, name= 'home'),
     #path('about/', about, name= 'about'),
      #path('contact/', contact, name= 'contact'),
       #path('portfolio/', portfolio, name= 'portfolio'),
        #path('services/', services, name= 'services'),
    path('login/', views.loginPage.as_view(), name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('changepassword/', views.changePassword.as_view(), name="changepassword"),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
     path('career/', views.Career, name='career'),
     path('blog/', views.Blogweb, name='blog'),
      path('blogdetail/',views.Blogdetail,name='blogdetail'),
    path('team/', views.Team, name='ourteam'),
     path('teamdetail/', views.teamdetail, name='teamdetail'),
      path('collabration/', views.collabortion, name='collaboration'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="dashboard/reset_password.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="dashboard/reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="dashboard/reset_password_confirm.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="dashboard/reset_password_complete.html"),
         name="password_reset_complete"),
	path('logout/', views.logoutUser, name="logout"),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('verify-email/',VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',VerifyEmailView.as_view(), name='account_confirm_email'),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('businesspartner/', views.businesspartner, name='businesspartner'),

    path('', views.Home.as_view(), name='Home'),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),

    path('aboutus/', views.AboutUs.as_view(), name='AboutUs'),
    path('aboutus/<slug:slug>', views.AboutUsDetail.as_view(), name='AboutUsDetail'),


    path('termsandcondition/', views.TermsAndCondition.as_view(), name='TermsAndCondition'),
    path('termsandcondition/<slug:slug>', views.TermsAndConditionDetail.as_view(), name='TermsAndConditionDetail'),


   # path('privacypolicy/', views.PrivacyPolicy.as_view(), name='PrivacyPolicy'),
    path('privacypolicy/<slug:slug>', views.PrivacyPolicyDetail.as_view(), name='PrivacyPolicyDetail'),

    path('sitemap/', views.SiteMap.as_view(), name='SiteMap'),
    path('sitemap/<slug:slug>', views.SiteMapDetail.as_view(), name='SiteMapDetail'),


    path('contactinfo/', views.ContactInfo, name='contactinfo'),
    path('contact/add/', views.ContactAdd, name='contact-add'),
    path('contact/edit/<str:slug>/', views.ContactEdit, name='contact-edit'),
    path('contact/update/<str:slug>/', views.ContactUpdate, name='contact-update'),
    path('contact/delete/<str:slug>/', views.ContactDelete, name='contact-delete'),



    path('collabortioninfo/', views.consultationView, name='collabortioninfo'),
    path('collabortion/add/', views.consultationAdd, name='collabortion-add'),
    path('collabortion/edit/<str:slug>/', views.consultationEdit, name='collabortion-edit'),
    path('collabortion/update/<str:slug>/', views.consultationUpdate, name='collabortion-update'),
    path('collabortion/delete/<str:slug>/', views.consultationDelete, name='collabortion-delete'),
    
   # path('pages/', include('bizlerapp.urls')),
    path('dashboard/blogview/', views.BlogView, name='blogview'),
    path('dashboard/blogview/add/', views.BlogAdd, name='blog-add'),
    path('dashboard/blogview/edit/<str:slug>/', views.BlogEdit, name='blog-edit'),
    path('dashboard/blogview/update/<str:slug>/', views.BlogUpdate, name='blog-update'),
    path('dashboard/blogview/delete/<str:slug>/', views.BlogDelete, name='blog-delete'),
    # ************************services *************************
    path('servicesinfo/', views.servicesView, name='servicesinfo'),
    path('services/add/', views.servicesAdd, name='services-add'),
    path('services/edit/<str:slug>/', views.servicesEdit, name='services-edit'),
    path('services/update/<str:slug>/', views.servicesUpdate, name='services-update'),
    path('services/delete/<str:slug>/', views.servicesDelete, name='services-delete'),

     # ************************portfolio *************************
    path('portfolioinfo/', views.portfolioView, name='portfolioinfo'),
    path('portfolio/add/', views.portfolioAdd, name='portfolio-add'),
    path('portfolio/edit/<str:slug>/', views.portfolioEdit, name='portfolio-edit'),
    path('portfolio/update/<str:slug>/', views.portfolioUpdate, name='portfolio-update'),
    path('portfolio/delete/<str:slug>/', views.portfolioDelete, name='portfolio-delete'),

    # ************************career *************************
    path('careerinfo/', views.CareerView, name='careerinfo'),
    path('career/add/', views.CareerAdd, name='career-add'),
    path('career/edit/<str:slug>/', views.CareerEdit, name='career-edit'),
    path('career/update/<str:slug>/', views.CareerUpdate, name='career-update'),
    path('career/delete/<str:slug>/', views.CareerDelete, name='career-delete'),

 # ************************business *************************
    path('businesspartnerinfo/', views.businesspartnerView, name='businesspartnerinfo'),
    path('businesspartner/add/', views.businesspartnerAdd, name='business-add'),
    path('businesspartner/edit/<str:slug>/', views.businesspartnerEdit, name='business-edit'),
    path('businesspartner/update/<str:slug>/', views.businesspartnerUpdate, name='business-update'),
    path('businesspartner/delete/<str:slug>/', views.businesspartnerDelete, name='business-delete'),

    # ************************ourteam*************************
    path('ourteaminfo/', views.TeamView, name='ourteaminfo'),
    path('ourteam/add/', views.TeamAdd, name='team-add'),
    path('ourteam/edit/<str:slug>/', views.TeamEdit, name='team-edit'),
    path('ourteam/update/<str:slug>/', views.TeamUpdate, name='team-update'),
    path('ourteam/delete/<str:slug>/', views.TeamDelete, name='team-delete'),

     # ************************pricing*************************
    path('pricinginfo/', views.PricePackView, name='pricinginfo'),
    path('pricing/add/', views.PricePackAdd, name='pricing-add'),
    path('pricing/edit/<str:slug>/', views.PricePackEdit, name='pricing-edit'),
    path('pricing/update/<str:slug>/', views.PricePackUpdate, name='pricing-update'),
    path('pricing/delete/<str:slug>/', views.PricePackDelete, name='pricing-delete'),

# ************************customer review*************************
  path('customerreview/', views.customerreview, name='customerreview'),
    path('customerreviewinfo/', views.customerreviewView, name='customerreviewinfo'),
    path('customerreview/add/', views.customerreviewAdd, name='customerreview-add'),
    path('customerreview/edit/<str:slug>/', views.customerreviewEdit, name='customerreview-edit'),
    path('customerreview/update/<str:slug>/', views.customerreviewUpdate, name='customerreview-update'),
    path('customerreview/delete/<str:slug>/', views.customerreviewDelete, name='customerreview-delete'),
    path('businesspartner/', include('businesspartnerapp.urls')),

    path('careerpage/', include('careerpageapp.urls')),

    path('ourteam/', include('ourteamapp.urls')),

    path('portfolio/', include('portfolioaapp.urls')),

    path('priceandpackages/', include('priceandpackagesapp.urls')),
       
    path('services/', include('servicesapp.urls')),

    path('customerreview/', include('customerreviewapp.urls')),

    path('consultation/', include('consultationapp.urls')),
    path('pricing/', views.Price, name='pricing'),
    path('termandcondition/', views.TermandCondition, name='termandcondition'),
     path('privacypolicy/', views.PrivacyPolicyView, name='privacypolicy'),
    #path('bizler/', include('bizlerapp.urls')),

     # ************************client*************************
    path('ourclient/', views.ourClient, name='ourclient'),
    path('ourclientinfo/', views.ourClientView, name='ourclientinfo'),
    path('ourclient/add/', views.ourClientAdd, name='client-add'),
    path('ourclient/edit/<str:slug>/', views.ourClientEdit, name='client-edit'),
    path('ourclient/update/<str:slug>/', views.ourClientUpdate, name='client-update'),
    path('ourclient/delete/<str:slug>/', views.ourClientDelete, name='client-delete'),










]

if settings.DEBUG:
      urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  
