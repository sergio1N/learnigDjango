from django.urls import path
from . import views 

urlpatterns = [
    path("resulatado/", views.home),  
    path("", views.Con_estilos),  
    path('getuser/', views.qryview, name='qryview'),
    path("dishes/<str:dish>", views.menuItems),  
    
]