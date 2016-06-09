"""nms URL Configuration

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
from django.conf.urls import url, include
from django.contrib.staticfiles import views
from django.conf import settings
from django.contrib import admin

from apps.landing.views import LandingView
from apps.home.views import (HomeView, HistoryView, LoginView, LogoutView, AboutView, HelpView)
from apps.ip.views import (IPListView, IPCreateView, IPDeleteView, IPAPIList)
from apps.user.views import UserProfileView
from apps.transaction.views import (TransactionAPI, TransactionStatusAPI)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^static/(?P<path>.*)$', views.static.serve,
        {'document_root': settings.STATIC_ROOT,
         'show_indexes': settings.DEBUG}),
    
    url(r'^$', view=LoginView.as_view(), name='landing'),
    url(r'^login', view=LoginView.as_view(), name='login'),
    url(r'^logout', view=LogoutView.as_view(), name='logout'),
    url(r'^about', view=AboutView.as_view(), name='about'),
    url(r'^help', view=HelpView.as_view(), name='help'),
    url(r'^profile', view=UserProfileView.as_view(), name='profile'),
    url(r'^accounts/', include('allauth.urls')),
    
    url(r'^ping/$', view=HomeView.as_view(), name='home'),
    url(r'^history/$', view=HistoryView.as_view(), name='history'),
    url(r'^ip/$', view=IPListView.as_view(), name='ip'),
    url(r'^ip/create/$', view=IPCreateView.as_view(), name='ip_create'),
    url(r'^ip/delete/(?P<pk>[0-9]+)/$', view=IPDeleteView.as_view(), name='ip_delete'),

    url(r'^core/ip/$', view=IPAPIList.as_view()),
    url(r'^core/transaction/$', view=TransactionAPI.as_view()),
    url(r'^core/status/$', view=TransactionStatusAPI.as_view()),
]
