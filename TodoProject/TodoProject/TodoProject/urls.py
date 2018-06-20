"""TodoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views
from django.views.generic.base import TemplateView
from TodoApp.Views.todoviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'addtask/<int:user_id>',AddTaskView.as_view(),name="addtask"),
    path(r'updatetask/<int:pk>',UpdateTask.as_view(),name="updatetask"),
    path(r'deletetask/<int:pk>', DeleteTask.as_view(), name="deletetask"),
    path(r'tasklist/',Viewtasklist.as_view(),name="tasklist"),
    #path(r'home/',homepage.as_view(),name="home"),
    path(r'login/',views.login,{'template_name':'registration/login.html'},name="login"),
    path(r'logout/', views.logout, {'template_name': 'registration/login.html'}, name="logout"),
    #path(r'',TemplateView.as_view(template_name='home.html'),name="home")
]