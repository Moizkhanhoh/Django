from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    path('', views.index,name='home'),
    path('About', views.About,name='About'),
    path("Services", views.Services, name="Services"),
    path("contact", views.contact, name="contact")
]