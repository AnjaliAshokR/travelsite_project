from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register1/', views.register1, name='home'),
    # path('mathop/',views.operation,name='operation'),
    # path('thanks/',views.thanks,name='thanks'),
    # path('contact/',views.contact,name='contact'),
    # path('details/',views.details,name='details'),
]
