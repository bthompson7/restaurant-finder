'''
https://www.mindsumo.com/contests/d052bcf8-4580-4922-95ef-a9f6ceaf0f10

Requirements:
    1. Submit a deployed web application and include both your website URL and the supporting Github repository.
    2. The app must use Yelp's Fusion API - done
    3. Your app should be able to plot merchants on a map - done
    4. Your app should be able to obtain user location via HTML5 Geolocation - done 
    
  Other:
     1. Click on map icon to bring up dialog box about restaurant - done
     2. Details for restaurant 
     

'''

import time,os,json
from apicall import Yelp
from flask import Flask,render_template, jsonify,request,Response

app = Flask(__name__)
app.debug = True
API_KEY = 'tn0G7Fq-F_RSxsvFfiYZ-8yBnuYP8xx58hzTr-kfCPILYlXHC-fvNvBccNJ_IOYfvvDJcHxFy_8eF8uRJxqPTXpnGeRH5Pl5UJAdNm-CykfdKW98Wpw-aOWEYr9NXnYx'

restList = []
restList3 = None
@app.route('/', methods= ['GET'])
def geo():
    return render_template('index.html')
    
@app.route('/postmethod', methods=['GET','POST'])
def postmethod():
    global data
    print("post method called 1")
    data = request.get_json()
    print(data)
    print("post method called 2")
    return data

@app.route('/rest', methods=['GET','POST'])
def restTypeMethod():
    global rest
    rest = request.get_json()
    print(rest)
    print("rest method")
    return rest


@app.route('/restaurant/<string:id>', methods=['GET'])
def displayRestaurantDetails(id):
    someData = id
    api = Yelp
    dataFromApi = api.search_by_id(API_KEY,id)
    restHasHoursListed = True
    try:
        print(dataFromApi['hours'][0]['is_open_now'])
    except:
        restHasHoursListed = False
    print(dataFromApi)
    return render_template('details.html',**locals())


@app.route('/getdata', methods=['GET'])
def getdata():
    global data
    global rest
    api = Yelp
    lat = data['location']['lat']
    lng = data['location']['lng']
    print(rest['restType'])
    dataFromApi = api.search_nearby(API_KEY,rest['restType'],lat,lng) #replace lunch with restType
    json.dumps(dataFromApi)
    restList = []
    for nearby_restaurant in dataFromApi['businesses']:
            restList.append(nearby_restaurant)
            
    return Response(json.dumps(restList),  mimetype='application/json')

if __name__ == '__main__':
        app.run()