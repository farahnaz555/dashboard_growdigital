from django.urls import path

from . import views

app_name = 'ourteamapp'

urlpatterns = [
    path('ourteam', views.OurTeamList.as_view(), name='team-view' ),
    path('ourteamdetail', views.OurTeamDetail.as_view(), name='team-form' ),


]
