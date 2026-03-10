from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addEmployee, name='add_employee'),
    path('update/<int:id>/', views.updateEmployee, name='update_employee'),
    path('delete/<int:id>/', views.deleteEmployee, name='delete_employee'),
]