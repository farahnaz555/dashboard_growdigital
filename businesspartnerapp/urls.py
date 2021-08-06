from django.urls import path

from . import views

app_name = 'businesspartnerapp'

urlpatterns = [
    path('businesspartner', views.BusinessPartnerList.as_view(), name='businesspartner-view' ),
    path('businesspartnerdetail', views.BusinessPartnerDetail.as_view(), name='businesspartner-detail' ),


]





#businesspartnerapp
