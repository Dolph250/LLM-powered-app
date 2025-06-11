from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('chatbot/', views.chatbot, name="chatbot"),
    path('ask-openai/', views.ask_openai, name='ask_openai'),
    path("logout/", admin.site.urls),  
    path('users/', views.users, name='users'),
    path('login/', views.login, name='login'),
  
     
     
    ]