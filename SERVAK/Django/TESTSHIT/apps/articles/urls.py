from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_test, name = 'articles_test'),
    path('ToPD/', views.ToPD, name = 'ToPD')
]