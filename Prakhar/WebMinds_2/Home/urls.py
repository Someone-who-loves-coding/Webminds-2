from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.Landing),
    path('Home/',views.Home,name='Home'),
    path('Contact Us/',views.Contact,name='Contact Us'),
    path('Discuss/',views.Discuss,name='Discuss'),
    path('Catalog/',views.Courses,name='Catalog')
]