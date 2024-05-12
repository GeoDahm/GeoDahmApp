from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('upload/output/',views.output,name='cd_output'),
    path('',views.index,name='home'),
    path('upload/',views.imageupload,name='upload'),
    path('riskzones/',views.riskzones,name='riskzones'),
    path('riskzones/Map4/',views.Map4,name='map'),
    path('riverflow/',views.riverflow,name='riverflow'),
    path('about/',views.about,name='about'),
]