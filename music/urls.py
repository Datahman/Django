# This file enlists all the app URLs/URIs

from django.conf.urls import url

from . import views # Import views class

app_name = 'music'
urlpatterns = [
	# /music
	url(r'^$', views.HomepageView.as_view(), name='index'),
	# The re ignores suffix slash albumID/ <--
	url(r'^(?P<pk>[0-9]+)/$', views.DetailpageView.as_view(), name='detail'),
	# music/album/add/
	url(r'^album/add/$', views.AddAlbum.as_view(), name='add-album'),
	# music/album/2
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update-album'),
	# music/album/2/delete
	url(r'^album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='delete-album')
]

""" name: Used as the reference var. to use the regular expression against path parameter"""


""" On music root path
	call views.index() function
	 """
""" On music sub-resource /albumID
	call views.detail() function  
"""