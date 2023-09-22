from django.urls import path
from .views import index

urlpatterns = [
    path('',index),
    path('home',index),
    path('Picgrader',index),
    path('test',index),
    path('Create_Exhibition',index)
]
