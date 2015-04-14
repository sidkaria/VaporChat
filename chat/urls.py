from django.conf.urls import patterns, include, url
from chat import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^aboutus/$', views.aboutus, name='aboutus'),
	url(r'^signupenter/$', views.signupenter, name='signupenter'),
	url(r'^signupsuccess/$', views.signupsuccess, name='signupsuccess'),
	url(r'^confirm/(?P<confirm_code>.*)/$', views.confirm, name='confirm'),
	url(r'^login/$', views.login, name='login')
	
)