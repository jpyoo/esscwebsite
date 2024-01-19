"""
URL configuration for esscwebsite project.

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
from django.urls import path
from django.views.generic.base import TemplateView # new 
from django.contrib.auth import views as auth_views

from . import views # import views.py from the same directory
#import homepage app views
from homepage import views as homepage_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path( '', TemplateView.as_view( template_name = 'index.html' ), name = 'index' ),
    #homepage view
    path('', homepage_views.home, name='home'),
    path('image/<str:model_name>/<int:image_id>/', homepage_views.serve_image, name='serve_image'),
    path('contact/', homepage_views.contact, name='contact'),
    path('archive/', homepage_views.archive, name='archive'),
    # #auth
    # path('login/', auth_views.LoginView.as_view( template_name = 'accounts/login.html'), name='login'),
]
