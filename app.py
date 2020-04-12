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
API_KEY = os.environ['API_KEY']

restList = []
restList3 = None
data = None
rest = None

@app.route('/', methods= ['GET'])
def geo():
    return render_template('index.html')
    
@app.route('/findlocation', methods=['GET','POST'])
def postmethod():
    global data
    data = request.get_json()
    return data

@app.route('/rest', methods=['GET','POST'])
def restTypeMethod():
    global rest
    rest = request.get_json()
    return rest


@app.route('/restaurant/<string:id>', methods=['GET'])
def displayRestaurantDetails(id):
    someData = id
    api = Yelp
    dataFromApi = api.search_by_id(id)
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
    dataFromApi = api.search_nearby(50,rest['restType'],lat,lng)
    json.dumps(dataFromApi)
    restList = []
    for nearby_restaurant in dataFromApi['businesses']:
            restList.append(nearby_restaurant)
    
    response = Response(json.dumps(restList),  mimetype='application/json')
    print(response) 
    return response

if __name__ == '__main__':
        app.run()