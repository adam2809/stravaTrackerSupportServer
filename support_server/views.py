from django.http import HttpResponse
import os
import requests

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from support_server.models import User


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


@require_http_methods(["GET"])
def exchange_token(req):
    if(req.GET['scope'].find('activity:write') == -1):
        return HttpResponse('Scope activity:write is required')

    print(f'GET token exhange request with params: {req.GET}')
    auth_code = req.GET['code']
    res = requests.post(BASE_API_URL + '/oauth/token',
        {
            'client_id':CLIENT_ID ,
            'client_secret':CLIENT_SECRET ,
            'code':auth_code,
            'grant_type':'authorization_code'
        }
    )
    if(res.status_code != 200):
        return HttpResponse(content='Strava OAuth request error',status=400)
    
    res_json = res.json()
    print(f'Successful token exhange with response: {res_json}')

    if(User.objects.filter(esp_code=auth_code[:8]).exists()):
        return HttpResponse(content='Esp code generation error. Try Again.',status=400)

    User.objects.filter(strava_id=res_json['athlete']['id']).delete()

    new_user = User.objects.create(
        refresh_token=res_json['refresh_token'],
        access_token=res_json['access_token'],
        esp_code=auth_code[:8],
        strava_id=res_json['athlete']['id']
    )
    new_user.save()
    print(f'Saved new user {new_user}')

    return HttpResponse(auth_code[:8])

    
    

    


