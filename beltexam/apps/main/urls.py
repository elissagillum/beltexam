from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.success),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^friends$', views.success),
	url(r'^user/', views.users),
	url('^delete$', views.delete),
	url(r'^logout$', views.logout, name='logout'),
]
