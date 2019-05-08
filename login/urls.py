from django.conf.urls import url
from login import views

# SET THE NAMESPACE!
app_name = 'login'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    url(r'^contractor/$', views.Contractor, name='contractor'),
    url(r'^driver/$', views.Driver, name='driver'),
    url(r'^contractor_login/$', views.contractor_login, name='contractor_login'),
    url(r'^driver_login/$', views.driver_login, name='driver_login'),

]