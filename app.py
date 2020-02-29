'''
https://www.mindsumo.com/contests/d052bcf8-4580-4922-95ef-a9f6ceaf0f10

Requirements:
    1. Submit a deployed web application and include both your website URL and the supporting Github repository.
    2. The app must use Yelp's Fusion API - done
    3. Your app should be able to plot merchants on a map - done
    4. Your app should be able to obtain user location via HTML5 Geolocation - done 
    
  Other:
     1. Click on map icon to bring up dialog box about restaurant - done
     2. Check the time and if its between like 2AM-11AM breakfast 11-3PM lunch 3PM-2AM dinner

'''

import time,os,json
from apicall import Yelp
from flask import Flask,render_template, jsonify,request,Response
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource


app = Flask(__name__)
app.debug = True
API_KEY = 'tn0G7Fq-F_RSxsvFfiYZ-8yBnuYP8xx58hzTr-kfCPILYlXHC-fvNvBccNJ_IOYfvvDJcHxFy_8eF8uRJxqPTXpnGeRH5Pl5UJAdNm-CykfdKW98Wpw-aOWEYr9NXnYx'

restList = []
restList3 = None
@app.route('/', methods= ['GET', 'POST'])
def geo():
    return render_template('index.html')
    
'''
called by index.html
'''
@app.route('/postmethod', methods=['GET','POST'])
def postmethod():
    global data
    data = request.get_json()
    print(data)
    return data

@app.route('/rest', methods=['GET','POST'])
def restTypeMethod():
    global restType
    restType = request.get_json()
    print(restType)
    return restType

@app.route('/getdata', methods=['GET'])
def getdata():
    global data
    global restType
    api = Yelp
    lat = data['location']['lat']
    lng = data['location']['lng']

    dataFromApi = api.search(API_KEY,"lunch",lat,lng) #replace lunch with restType
    json.dumps(dataFromApi)
    for nearby_restaurant in dataFromApi['businesses']:
            restList.append(nearby_restaurant)
    return Response(json.dumps(restList),  mimetype='application/json')

if __name__ == '__main__':
        app.run()