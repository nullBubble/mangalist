from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_manga/', views.add_manga, name='add_manga'),
    path('delete_manga/', views.delete_manga, name='delete_manga')
]