from django.urls import path

from . import views

app_name = 'consultationapp'

urlpatterns = [
    path('consultation', views.ConsultionList.as_view(), name='consultion-view' ),
    path('consultationdetail', views.ConsultionDetail.as_view(), name='consultion-form' ),


]

#consultationapp
