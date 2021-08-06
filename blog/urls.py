from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
   path('dashboard/blogview/', views.BlogView, name='blogview'),
    path('dashboard/blog/add/', views.BlogAdd, name='blog-add'),
    path('dashboard/blog/edit/<str:slug>/', views.BlogEdit, name='blog-edit'),
    path('dashboard/blog/update/<str:slug>/', views.BlogUpdate, name='blog-update'),
    path('dashboard/blog/delete/<str:slug>/', views.BlogDelete, name='blog-delete'),
]
