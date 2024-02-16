from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('card/<str:pk>/', views.card, name="card"),
    path('dashboard/', views.dashboard, name="dashboard")
]