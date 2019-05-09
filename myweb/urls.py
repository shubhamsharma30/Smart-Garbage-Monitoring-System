"""myweb URL Configuration

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

from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from login import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^map/',views.map, name='map'),
    url(r'^login/',include('login.urls')),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^Map/$',views.Multi_map,name='Map'),
    url(r'^Driver/$',views.Driver, name='Driver'),

    url(r'^Clients/$', views.Customer, name='Customer'),
    url(r'^Trashcan/$', views.Trashcan, name='Trashcan'),
    url(r'^contractor/$', views.Contractor, name='contractor'),
    url(r'^driver/$', views.Driver, name='driver'),

    url(r'^customer/$',views.Customer_list,name="customer"),
    url(r'^driver1/$',views.Driver_list,name="driver1"),
    url(r'^trash/$',views.Trashcan_list,name="trash"),

    url(r'^customer/(?P<id>\d+)/$', views.Customer_Detail, name='Customer_Detail'),
    url(r'^driver1/(?P<id>\d+)/$', views.Driver_Detail, name='Driver_Detail'),
    url(r'^trash/(?P<id>\d+)/$', views.Trashcan_Detail, name='Trashcan_Detail'),
    url(r'^ubidots/',views.Ubidots,name='ubidots')

]