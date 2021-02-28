from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

from support_server.views import *
from strava_tracker_support_server.settings import HOSTNAME

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^athlete', get_athlete_info),
    url(r'^uploads', forward_ride_upload),
    url(r'login', RedirectView.as_view(url=f'https://www.strava.com/oauth/authorize?client_id=57956&response_type=code&redirect_uri=http://{HOSTNAME}/exchange_token&approval_prompt=force&scope=activity:write')),
]
