from django.contrib import admin
from django.urls import path , include
from todo import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('delete/<int:todo_id>' , views.delete , name='delete')
]