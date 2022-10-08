from django.urls import path
from . import views
urlpatterns = [
    path('/', views.home, name='home'),
    path('companion', views.companion, name='companion'),
    path('plantrip', views.plantrip, name='plantrip'),
    path('chat', views.chat, name='chat'),
    path('blog', views.blog, name='blog'),
    path('profile', views.profile, name='profile'),
    
    
]