from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("lists/", views.lists, name = "lists"),
    path("lists/<int:id>", views.items, name = "items"),
    path("create/", views.create, name = "create"),
    
    ]