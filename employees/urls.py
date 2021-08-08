from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('', views.read, name='read'),
    path('<str:emp_id>', views.update, name='update'),
    path('emloyees/<str:emp_id>', views.delete, name='delete'),
]