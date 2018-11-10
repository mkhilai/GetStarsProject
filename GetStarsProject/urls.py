from django.conf.urls import url
from GetStarsProject.api.views import GetReposList


urlpatterns = [
	url(r'^repos/$', GetReposList.as_view(), name = 'repos'),
]
