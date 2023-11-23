from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='newtask'),
    path('update/<int:pk>/', views.updateTask, name='update_task'),
    path('<int:pk>/', views.deleteTask, name='delete'),

]