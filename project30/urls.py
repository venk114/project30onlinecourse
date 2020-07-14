"""project30 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app30 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.AdminLogin.as_view(),name="main"),
    path('login_check/',views.LoginCheck.as_view(),name="login_check"),
    path('new_class/',views.NewClass.as_view(),name="new_class"),
    path('view_all/',views.AllCourse.as_view(),name="view_all"),
    path('home/',views.Home.as_view(),name="home"),
    path('upd_class<int:pk>/',views.UpdCourse.as_view(),name="upd_class"),
    path('del_class<int:pk>/',views.DelCourse.as_view(),name="del_class"),
]
