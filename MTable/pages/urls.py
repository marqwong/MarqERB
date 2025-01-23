from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('story', views.story, name='story'),
    path('guest', views.guest, name='guest'),
    path('chef', views.chef, name='chef'),
    path('press', views.press, name='press'),
    path('fqa', views.fqa, name='fqa'),
    path('join', views.join, name='join'),
    path('contactus', views.contactus, name='contactus'),

]