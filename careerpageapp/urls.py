from django.urls import path

from . import views

app_name = 'careerpageapp'

urlpatterns = [
    path('career', views.CareerPageList.as_view(), name='career-view' ),
    path('careerdetail', views.CareerPageDetail.as_view(), name='career-form' ),


]
