from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from nauka import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nauka.urls')),

    #path('', views.home, name='home')
    #path('login/', auth_views.LoginView.as_view(), name='login'),
]
