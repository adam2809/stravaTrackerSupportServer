from flask import Flask,request,flash
import os
import requests
from stravaio import strava_oauth2

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

app=Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/athlete',methods=['GET'])
def get_athlete_info():
    print(ACCESS_TOKEN)
    res = requests.get(BASE_API_URL+"/athlete",headers=headers)
    return res.text


@app.route('/uploads',methods=['POST'])
def forward_ride_upload():
    print(request.headers)
    print(request.data)

    form_data = default_form_data.copy()
    form_data['file'] = request.data.decode('utf-8')

    res = requests.post(
        BASE_API_URL+"/uploads",
        headers=headers,
        files=form_data
    )

    ret = str(res.status_code)+'\n'+res.text
    print(ret)
    return ret