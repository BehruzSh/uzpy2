from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name='index'),
    path('service/',service,name='service'),
    path('product/',product,name='product'),
    path('gallery/',gallery,name='gallery'),
    path('contact/',contact,name='contact'),
    path('xaridor/',xaridor,name='xaridor'),
    path('about/',about,name='about'),
]