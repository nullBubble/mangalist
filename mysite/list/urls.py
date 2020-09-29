from django.urls import path
from . import views

app_name = 'list'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/current_chapter/', views.current_c, name='current_c'),
    path('<int:question_id>/link/', views.link, name='link'),
]