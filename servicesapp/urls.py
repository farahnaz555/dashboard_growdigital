from django.urls import path

from . import views

app_name = 'servicesapp'

urlpatterns = [
    path('', views.ServicesList.as_view(), name='ServicesList' ),
    path('<slug:slug>', views.ServicesDetail.as_view(), name='ServicesDetail' ),


]
