from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView

from support_server.views import *

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^athlete', get_athlete_info),
    url(r'^uploads', forward_ride_upload),
    url(r'^exchange_token', exchange_token),
    url(r'^tokens', get_tokens_for_esp_code),
    url(r'^login', RedirectView.as_view(url='https://www.strava.com/oauth/authorize?'
        'client_id=57956&'
        'response_type=code&' 
        f'redirect_uri=http://localhost:8000/exchange_token&'
        'approval_prompt=force&'
        'scope=activity:write'
    )),
]
