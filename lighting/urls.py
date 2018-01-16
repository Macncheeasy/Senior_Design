"""lighting URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#~ from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from rest_framework import routers
from myapp import views


admin.autodiscover()

#Automatically creates an API root view for us
router = routers.DefaultRouter()
#Two arguments needed for register(), a prefix:url prefix to use for this set of routes
#viewset: a viewset class
router.register(r'profiles', views.ProfilesViewSet)

urlpatterns = [
    url(r'^favicon.ico$', RedirectView.as_view(
                          url=staticfiles_storage.url('favicon.ico'),
                          permanent=False), name="favicon"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.login, name='logout'),
    
    
    #~ url(r'^logout/$', auth_views.logout, name='logout'),
]
