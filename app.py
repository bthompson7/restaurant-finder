'''
https://www.mindsumo.com/contests/d052bcf8-4580-4922-95ef-a9f6ceaf0f10

Requirements:
    1. Submit a deployed web application and include both your website URL and the supporting Github repository.
    2. The app must use Yelp's Fusion API - done
    3. Your app should be able to plot merchants on a map - done
    4. Your app should be able to obtain user location via HTML5 Geolocation - done 
    
  Other:
     1. Click on map icon to bring up dialog box about restaurant - done
     2. Details for restaurant - done
     3. Search by type pizza,sushi etc... - done
     4. Scroll to top button
     

'''

import time,os,json
import threading
from apicall import Yelp
from flask import Flask,render_template, jsonify,request,Response

app = Flask(__name__)
app.debug = True
API_KEY = os.environ['API_KEY']

print("Starting")
restList = []
data = None
foodtype = None
rest = 'lunch'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/', methods= ['GET'])
def main():
    return render_template('index.html')
    
@app.route('/findlocation', methods=['GET','POST'])
def postmethod():
    global data
    data = request.get_json()
    print("/findlocation called")
    print(data)
    return data

@app.route('/rest', methods=['GET','POST'])
def restTypeMethod():
    print("/rest called")
    global foodtype,rest
    foodtype = None
    rest = request.get_json()
    print(rest)
    return rest

@app.route('/foodtype', methods=['GET','POST'])
def foodTypeMethod():
    print("/foodtype called")
    global foodtype,rest
    rest = None
    foodtype = request.get_json()
    return foodtype


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
    print("getdata called")
    api = Yelp
    global data,rest,restList
    print("data is",data)
    lat = data['location']['lat']
    lng = data['location']['lng']
   
    if rest is not None:
        print("Rest is not None")
        restType = rest['restType']
        print("restType is",restType)
        dataFromApi = api.search_nearby(50,restType,lat,lng)
    elif rest is None:
        print("restType is",rest)
        print("Food type is ",foodtype)
        food = foodtype['foodType']
        dataFromApi = api.search_nearby_for_type(50,lat,lng,food)
        print("Rest is None")
        
    rest = None
    json.dumps(dataFromApi)
    restList = []
    for nearby_restaurant in dataFromApi['businesses']:
            restList.append(nearby_restaurant)
    
    response = Response(json.dumps(restList),  mimetype='application/json')
    print(response) 
    return response

if __name__ == '__main__':
        app.run()