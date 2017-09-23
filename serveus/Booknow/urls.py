from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/loginUser/$', views.logUser, name='logUser'),
    url(r'^/loginsp/$', views.logsp, name='logsp'),
    url(r'^/verLoginUser/$', views.verLogUser, name='verLogUser'),
    url(r'^/verLoginsp/$', views.verLogSP, name='verLogSP'),
    url(r'^/regis/$', views.regisCus, name='regisCus'),
    url(r'^/regisSP/$', views.regisSP, name='regisSP'),
    url(r'^/index/$', views.index, name='index'),
    url(r'^/signUpUser/$', views.signUpUser, name='signUpUser'),
    url(r'^/signUpSP/$', views.signUpSP, name='signUpSP'),
]