from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
  
    path('update-profile/', views.update_profile, name='update-profile'),

    path('delete-account/', views.delete_account, name='delete-account'),
]