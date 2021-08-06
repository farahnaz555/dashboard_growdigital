from django.urls import path

from . import views

app_name = 'customerreviewapp'

urlpatterns = [
    path('customer', views.CustomerReviewList.as_view(), name='CustomerReviewList' ),
    path('customerdetail', views.CustomerReviewDetail.as_view(), name='customer-form' ),

    # path('reviews/', views.reviews, name='reviews'),



]
