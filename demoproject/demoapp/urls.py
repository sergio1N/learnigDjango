from django.urls import path
from . import views 


urlpatterns = [
    path("resulatado/", views.home),  
    path("", views.Con_estilos),  
    path('getuser/', views.qryview, name='qryview'),
    path("dishes/<str:dish>", views.menuItems), 
    path("form/", views.mostrar_formulario),
    path("hello/", views.from_view, name='from_view'),
    path("menu/", views.menu_by_id),
]