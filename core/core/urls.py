"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from vege.views import *


urlpatterns = [
    path('',home, name='home'),
    path('receipe/', receipes, name='receipes'),
    path('login_page/', login_page, name= 'login_page'),
    path('register/', register, name='register'),
    path('delete_receipe/<id>/', delete_receipe, name='delete'),
    path('update-receipe/<id>/', update_receipe, name='update'),
    path('contact/',contact, name='contact'),
    path('about/',about, name='about'),
    path('logout_page/', logout_page, name="logout" ),
    path('success/',success_page, name="success"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

