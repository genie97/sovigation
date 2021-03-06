# -*- coding: utf-8 -*-
"""web URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from sovigation import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^lib/$', views.lib),
    url(r'^fooda/$', views.fooda),
    url(r'^foodb/$', views.foodb),
    url(r'^foodc/$', views.foodc),

    url(r'^board/$', views.board),#home
    url(r'^write/$', views.write),#show_write_form
    url(r'^dowrite/$', views.dowrite),#DoWriteBoard
    url(r'^listPage/$', views.listpage),#listSpecificPageWork
    url(r'^searchedPage/$', views.searchedpage),#listSearchedSpecificPageWork
    url(r'^viewWork/$', views.viewwork),
    url(r'^listUpdate/$', views.listupdate),
    url(r'^updateBoard/$', views.updateboard),
    url(r'^delete/$', views.delete),
    url(r'^searchWithSubject/$', views.searchWithSubject),
]
