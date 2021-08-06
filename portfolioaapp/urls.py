from django.urls import path

from . import views

app_name = 'portfolioaapp'

urlpatterns = [
    path('', views.PortfolioList.as_view(), name='PortfolioList' ),
    path('<slug:slug>', views.PortfolioDetail.as_view(), name='PortfolioDetail' ),


]
