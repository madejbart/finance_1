"""Defines URL patterns for finance_app."""
from django.urls import path
from . import views

app_name = 'finance_app'
urlpatterns = [
    path('', views.index, name="index"),
    path('profiles', views.ProfilesView.as_view(), name="profiles"),

]