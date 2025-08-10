from django.contrib import admin 
from django.urls import  path,include 
from demoapp import views

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('demo/',include( "demoapp.urls") ),
    path("", views.from_view, name='home'),
    path("hello/<str:name>/", views.index, name='index'),
    ] 

handler404='demoproject.views.handler404'
