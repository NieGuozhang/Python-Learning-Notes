"""ch09www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include

from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:pid>/<str:del_pass>', views.index),
    path('list/', views.listing, name='list'),
    path('post/', views.posting, name='post'),
    path('contact/', views.contact, name='contact'),
    path('post2db/', views.post2db, name='post2db'),
    path(r'^captcha/', include('captcha.urls')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('userinfo/', views.userinfo, name='userinfo')
]
