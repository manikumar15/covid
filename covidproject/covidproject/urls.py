
from django.contrib import admin
from django.urls import path
from covidapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.animation_page),
    path('home_page/', views.home_page),
    path('search_page/', views.search_page),
    path('dashboard/', views.dashboard),
]
