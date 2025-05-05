"""
URL configuration for solomon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import home, register_view, login_view, contact_list, contact_detail, contact_create, contact_update, contact_delete
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(http_method_names=['get', 'post']), name='logout'),
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('contacts/new/', contact_create, name='contact_create'),
    path('contacts/<int:pk>/edit/', contact_update, name='contact_update'),
    path('contacts/<int:pk>/delete/', contact_delete, name='contact_delete'),
]