"""app URL Configuration

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

from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from userprofile import views as profile_views
from journal.urls import entry_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^login/$', profile_views.user_login, name="login"),
    url(r'^register/$', profile_views.register, name="register"),
    url(r'^logout/$', profile_views.user_logout, name="logout"),
    url(r'^entry/', include(entry_urls))
]
