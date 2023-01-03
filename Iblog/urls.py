"""Iblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homeview.as_view(),name='home'),
    path('signin/',views.LoginView.as_view(), name='signin'),
    path('signout/',views.log_out.as_view(),name='signout'),
    path('signup/',views.signup.as_view(),name='signup'),
    path('dashboard/',views.dashboard.as_view(),name='dashboard'),
    path('about/',views.aboutview.as_view(),name='about'),
    path('contactus/',views.contactusview.as_view(),name='contactus'),
    path('postdetails/<int:id>',views.postdetailsview.as_view(),name='postdetails'),
    path('addpost/',views.addpostview.as_view(),name='addpost'),
    path('editpost/<int:id>',views.editpost.as_view(),name='editpost'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('deletepost/<int:id>',views.deleteview.as_view(),name='deletepost')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
