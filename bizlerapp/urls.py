from django.urls import path,include
from django.contrib import admin
from bizlerapp import views
from django.contrib.auth import views as auth_views

app_name = 'bizlerapp'

urlpatterns = [
    path('', views.Home, name='home-view' ),
   # path('login/', views.loginPage.as_view(), name="login"),
   path('login/', views.loginPage.as_view(), name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('changepassword/', views.changePassword.as_view(), name="changepassword"),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.Blogweb, name='blog'),
    path('blogdetail/',views.BlogSingle,name='blogdetail'),
    path('team/', views.Team, name='ourteam'),
    path('teamdetail/', views.teamdetail, name='teamdetail'),
    path('career/', views.Career, name='career'),
    path('collabration/', views.collabortion, name='collaboration'),
    path('pricing/', views.Price, name='pricing'),
    path('termandcondition/', views.TermandCondition, name='termandcondition'),
    path('privacypolicy/', views.PrivacyPolicyView, name='privacypolicy'),
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
    path('dashboard/', views.Dashboard, name='dashboard'),

    path('dashboard/blogview/', views.BlogView, name='blogview'),
    path('dashboard/blogview/add/', views.BlogAdd, name='blog-add'),
    path('dashboard/blogview/edit/<str:slug>/', views.BlogEdit, name='blog-edit'),
    path('dashboard/blogview/update/<str:slug>/', views.BlogUpdate, name='blog-update'),
    path('dashboard/blogview/delete/<str:slug>/', views.BlogDelete, name='blog-delete'),

    # ****************** Contact Us ***********************

    path('contactinfo/', views.ContactInfo, name='contactinfo'),
    path('contact/add/', views.ContactAdd, name='contact-add'),
    path('contact/edit/<str:slug>/', views.ContactEdit, name='contact-edit'),
    path('contact/update/<str:slug>/', views.ContactUpdate, name='contact-update'),
    path('contact/delete/<str:slug>/', views.ContactDelete, name='contact-delete'),

    # *************************************************
  
    # ************************collaboration *************************
    path('collabortioninfo/', views.consultationView, name='collabortioninfo'),
    path('collabortion/add/', views.consultationAdd, name='collabortion-add'),
    path('collabortion/edit/<str:slug>/', views.consultationEdit, name='collabortion-edit'),
    path('collabortion/update/<str:slug>/', views.consultationUpdate, name='collabortion-update'),
    path('collabortion/delete/<str:slug>/', views.consultationDelete, name='collabortion-delete'),

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
  # ************************career *************************
    path('careerinfo/', views.CareerView, name='careerinfo'),
    path('career/add/', views.CareerAdd, name='career-add'),
    path('career/edit/<str:slug>/', views.CareerEdit, name='career-edit'),
    path('career/update/<str:slug>/', views.CareerUpdate, name='career-update'),
    path('career/delete/<str:slug>/', views.CareerDelete, name='career-delete'),

     # ************************business *************************
     path('businesspartner/', views.businesspartner, name='businesspartner'),
    path('businesspartnerinfo/', views.businesspartnerView, name='businesspartnerinfo'),
    path('businesspartner/add/', views.businesspartnerAdd, name='business-add'),
    path('businesspartner/edit/<str:slug>/', views.businesspartnerEdit, name='business-edit'),
    path('businesspartner/update/<str:slug>/', views.businesspartnerUpdate, name='business-update'),
    path('businesspartner/delete/<str:slug>/', views.businesspartnerDelete, name='business-delete'),

      # ************************customer review*************************
    path('customerreview/', views.customerreview, name='customerreview'),
    path('customerreviewinfo/', views.customerreviewView, name='customerreviewinfo'),
    path('customerreview/add/', views.customerreviewAdd, name='customerreview-add'),
    path('customerreview/edit/<str:slug>/', views.customerreviewEdit, name='customerreview-edit'),
    path('customerreview/update/<str:slug>/', views.customerreviewUpdate, name='customerreview-update'),
    path('customerreview/delete/<str:slug>/', views.customerreviewDelete, name='customerreview-delete'),

     # ************************client*************************
    path('ourclient/', views.ourClient, name='ourclient'),
    path('ourclientinfo/', views.ourClientView, name='ourclientinfo'),
    path('ourclient/add/', views.ourClientAdd, name='client-add'),
    path('ourclient/edit/<str:slug>/', views.ourClientEdit, name='client-edit'),
    path('ourclient/update/<str:slug>/', views.ourClientUpdate, name='client-update'),
    path('ourclient/delete/<str:slug>/', views.ourClientDelete, name='client-delete'),

]
