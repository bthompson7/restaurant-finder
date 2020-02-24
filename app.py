'''
https://www.mindsumo.com/contests/d052bcf8-4580-4922-95ef-a9f6ceaf0f10


:

Requirements:
    1. Submit a deployed web application and include both your website URL and the supporting Github repository.
    2. The app must use Yelp's Fusion API - done(api calls work)
    3. Your app should be able to plot merchants on a map - in progress
    4. Your app should be able to obtain user location via HTML5 Geolocation - done 

'''

import time,os,json
from apicall import Yelp
from restaurant import Resaurant
from flask import Flask,render_template, jsonify,request
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource


app = Flask(__name__)
app.debug = True
API_KEY = 'tn0G7Fq-F_RSxsvFfiYZ-8yBnuYP8xx58hzTr-kfCPILYlXHC-fvNvBccNJ_IOYfvvDJcHxFy_8eF8uRJxqPTXpnGeRH5Pl5UJAdNm-CykfdKW98Wpw-aOWEYr9NXnYx'

isPlotted = False
restList = []
restList3 = None
@app.route('/', methods= ['GET', 'POST'])
def geo():
    someList = [1, 2, (3, 4)] # Note that the 3rd element is a tuple (3, 4)
    someList2 = json.dumps(someList)
    print(someList2) # '[1, 2, [3, 4]]'            print(python_data)
    global isPlotted
    api = Yelp
    data = request.get_json()
    if data is not None:
        isPlotted = True
        jsonify(data)
        print(data)
        lat = data['location']['lat']
        lng = data['location']['lng']
        print("working")
        dataFromApi = api.search(API_KEY,'dinner',lat,lng)
        json.dumps(dataFromApi)
        print("Nearby Resaurants: ")
        for nearby_restaurant in dataFromApi['businesses']:
            restName = nearby_restaurant['name']
            restLat = nearby_restaurant['coordinates']['latitude']
            restLng = nearby_restaurant['coordinates']['longitude']
            restObj = Resaurant(restName,restLat,restLng)
            restList.append(restName)
            #print(len(restList))
            restList3 = json.dumps(restList)
            #restList2 = map(json.dumps,restList)
            #print(restList2)
            #restList3.append(restList2)
            #print(restList3)
            restList3 = json.dumps(restList)
    return render_template('index.html',data=restList)
    

'''
called by index.html
'''
@app.route('/postmethod', methods=['GET','POST'])
def postmethod():
    global data
    data = request.get_json()
    print("postmethod called")
    print(data) #use this as lat/lng instead
    return jsonify(data)


if __name__ == '__main__':
        app.run()