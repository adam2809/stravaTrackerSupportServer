from django.http import HttpResponse
import os
import requests

from django.views.decorators.csrf import csrf_exempt


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
BASE_API_URL="https://www.strava.com/api/v3"

headers = {
    'Authorization': 'Bearer ' + ACCESS_TOKEN
}

default_form_data = {
    'name':(None,'flakontests'),
    'description':(None,'To jest test flakona'),
    'trainer':(None,'null'),
    'commute':(None,'flase'),
    'data_type':(None,'gpx'),
    'external_id':(None,'sth'),
    'file':None
}

def get_athlete_info(req):
    res = requests.get(BASE_API_URL+"/athlete",headers=headers)
    return HttpResponse(res.text)


@csrf_exempt
def forward_ride_upload(request):
    form_data = default_form_data.copy()
    form_data['file'] = request.body.decode('utf-8')

    res = requests.post(
        BASE_API_URL+"/uploads",
        headers=headers,
        files=form_data
    )

    ret = str(res.status_code)+'\n'+res.text
    print(ret)
    return HttpResponse(ret)


def redirect_strava_oauth(req):
    return HttpResponsePermanentRedirect(
        'https://www.strava.com/oauth/authorize?client_id=57956&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:write'
    )

