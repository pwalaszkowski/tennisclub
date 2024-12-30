from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),         # Login Page
    path('main/', views.main, name='main'),           # Main page
    path('members/', views.members, name='members'),  # Members page
    path('member_registration/', views.member_registration, name='member_registration'),
    path('courts/', views.courts, name='courts'),    # Courts page
    path('about/', views.about, name='about'),      # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('logout/', views.logout_view, name='logout'),    # Logout
]