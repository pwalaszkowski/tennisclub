from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),           # Main page
    path('members/', views.members, name='members'),  # Members page
    path('courts/', views.courts, name='courts'),    # Courts page
    path('about/', views.about, name='about'),      # About page
    path('contact/', views.contact, name='contact'),  # Contact page
]