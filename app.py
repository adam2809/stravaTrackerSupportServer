from flask import Flask
import os
import requests
from stravaio import strava_oauth2

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
BASE_API_URL="https://www.strava.com/api/v3"

headers = {
    'Authorization': 'Bearer acbf061267bee446ce77c568489021c4ae48e85f'
}

upload_request_form_data = {
    'name':(None,'flakontests'),
    'description':(None,'To jest test flakona'),
    'trainer':(None,'null'),
    'commute':(None,'flase'),
    'data_type':(None,'gpx'),
    'external_id':(None,'sth'),
    'file':r"""
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<gpx version="1.0" creator="GPS Visualizer https://www.gpsvisualizer.com/" xmlns="http://www.topografix.com/GPX/1/0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd">
<trk>
  <name>output</name>
  <trkseg>
    <trkpt lat="52.531466667" lon="13.426316667">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:14.058Z</time>
      <course>268.6</course>
      <speed>4183.41</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.53" lon="13.364516667">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:15.058Z</time>
      <course>184.5</course>
      <speed>3395.80</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.4995" lon="13.362116667">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:16.058Z</time>
      <course>109.8</course>
      <speed>8421.61</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.461033333" lon="13.469233333">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:17.058Z</time>
      <course>48.3</course>
      <speed>5868.37</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.504516667" lon="13.518333333">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:18.058Z</time>
      <course>20.3</course>
      <speed>1262.60</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.5156" lon="13.52245">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:19.058Z</time>
      <course>295.4</course>
      <speed>8852.30</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.56445" lon="13.419116667">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:20.058Z</time>
      <course>266.5</course>
      <speed>9608.95</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.5559" lon="13.277666667">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:21.058Z</time>
      <course>168.9</course>
      <speed>10975.21</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.4579" lon="13.296883333">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:22.058Z</time>
      <course>91.2</course>
      <speed>21695.61</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
    <trkpt lat="52.450983333" lon="13.616866667">
      <ele>0.0</ele>
      <time>2020-12-25T20:20:23.058Z</time>
      <course>91.2</course>
      <speed>21695.61</speed>
      <sat>12</sat>
      <hdop>1.0</hdop>
    </trkpt>
  </trkseg>
</trk>
</gpx>
"""
}

app=Flask(__name__)

@app.route('/athlete',methods=['GET'])
def get_athlete_info():
    print(ACCESS_TOKEN)
    res = requests.get(BASE_API_URL+"/athlete",headers=headers)
    return res.text


@app.route('/uploads',methods=['POST'])
def forward_ride_upload():
    res = requests.post(
        BASE_API_URL+"/uploads",
        headers=headers,
        files=upload_request_form_data
    )
    return str(res.status_code)+'\n'+res.text