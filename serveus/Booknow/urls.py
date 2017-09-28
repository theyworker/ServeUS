from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/loginUser/$', views.logUser, name='logUser'),
    url(r'^/verLoginUser/$', views.verLogUser, name='verLogUser'),
    url(r'^/regis/$', views.regisCus, name='regisCus'),
    url(r'^/regBook/$', views.regBook, name='regBook'),
    url(r'^/index/$', views.index, name='index'),
    url(r'^/profile/$', views.profile, name='profile'),
    url(r'^/profileSer/$', views.profileSer, name='profileSer'),
    url(r'^/signUpUser/$', views.signUpUser, name='signUpUser'),
    url(r'^/bidBook/$', views.bidBook, name='bidBook'),
    url(r'^/loginsp/$', views.logsp, name='logsp'),
    url(r'^/verLoginSP/$', views.verLogSP, name='verLogSP'),
    url(r'^/registersp/$', views.regSP, name='regSP'),
    url(r'^/rgsp/$', views.rgsp, name='rgsp'),
    url(r'^/applyBooking/$', views.applyBooking, name='applyBooking'),

]