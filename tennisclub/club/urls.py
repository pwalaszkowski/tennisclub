from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),         # Login Page
    path('main/', views.main, name='main'),           # Main page
    path('members/members/', views.members, name='members'),  # Members page
    path('members/member_registration/', views.member_registration, name='member_registration'),
    path('members/member_edit/', views.member_edit, name='member_edit'), # Member profile edit
    path('courts/courts/', views.courts, name='courts'),    # Courts page
    path('courts/court_add/', views.court_add, name='court_add'),
    path('courts/court_reservation/', views.court_reservation, name='court_reservation'),
    path('courts/court_reservations_edit/<int:pk>', views.court_reservation_edit,
         name='court_reservation_edit'), # Edit a reservation
    path('about/', views.about, name='about'),      # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('logout/', views.logout_view, name='logout'),    # Logout
]
