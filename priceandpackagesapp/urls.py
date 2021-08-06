from django.urls import path

from . import views

app_name = 'priceandpackagesapp'

urlpatterns = [
    path('', views.PriceAndPackagesList.as_view(), name='PriceAndPackagesList' ),
    path('<slug:slug>', views.PriceAndPackagesDetail.as_view(), name='PriceAndPackagesDetail' ),


]
