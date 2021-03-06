"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views as main_views
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('userprofile.urls')),
    url(r'^project/new/', include('newproject.urls')),
    url(r'^$', main_views.home, name="socialweb_home")
]

urlpatterns += [
	url(r'^login/$', auth_views.login,
		{'template_name': 'login.html'},
		name='socialweb_login'),

	url(r'^logout/$', auth_views.logout,
		{'next_page': 'socialweb_home'},
		name='socialweb_logout')
]
