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
from parse import Parse
from flask import Flask,render_template, jsonify,request
from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource


app = Flask(__name__)
app.debug = True
API_KEY = 'tn0G7Fq-F_RSxsvFfiYZ-8yBnuYP8xx58hzTr-kfCPILYlXHC-fvNvBccNJ_IOYfvvDJcHxFy_8eF8uRJxqPTXpnGeRH5Pl5UJAdNm-CykfdKW98Wpw-aOWEYr9NXnYx'

@app.route('/', methods= ['GET', 'POST'])
def geo():
    api = Yelp
    lat = 43.726585899999996
    lng = -70.46454059999999

    dataFromApi = api.search(API_KEY,'dinner',lat,lng)
    json.dumps(dataFromApi)
    print("Nearby Resaurants: ")
    for nearby_restaurant in dataFromApi['businesses']:
        print(nearby_restaurant['name'])
        print(nearby_restaurant['coordinates'])
        
    return render_template('index.html')


'''
called by index.html
'''
@app.route('/postmethod', methods=['GET','POST'])
def postmethod():
    data = request.get_json()
    print("postmethod called")
    #print(data)
    return jsonify(data)


if __name__ == '__main__':
        app.run()