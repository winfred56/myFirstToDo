from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name = 'homepage'),
    path('edit/<int:pk>/',views.edit, name = 'editpage'),
    path('delete/<int:pk>/',views.delete, name = 'deletepage'),
]
