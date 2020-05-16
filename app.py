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

print("Starting Up")
MAX_RESULTS = 50


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/', methods= ['GET'])
def main():
    return render_template('index.html')
    
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


#example of the data we will get from index.html
#{'location': {'lat': 43.740220699999995, 'lng': -70.4526554}, 'data': 'chinese', 'type': 'food'}
#{'location': {'lat': 43.740220699999995, 'lng': -70.4526554}, 'data': 'lunch', 'type': 'rest'}
@app.route('/getdata', methods=['GET','POST'])
def getdata():
    restData = request.get_json()
    print("/getdata called")
    #print(restData)
    api = Yelp
    lat = restData['location']['lat']
    lng = restData['location']['lng']

    if restData['type'] == 'rest': #rest means breakfast, lunch,dinner
        restType = restData['data']
        dataFromApi = api.search_nearby(MAX_RESULTS,restType,lat,lng)
        print(dataFromApi)
    elif restData['type'] == 'food': #a specific food type like chinese,burgers etc...
        food = restData['data']
        dataFromApi = api.search_nearby_for_type(MAX_RESULTS,lat,lng,food)
        print(dataFromApi)
    json.dumps(dataFromApi)
    restList = []
    for nearby_restaurant in dataFromApi['businesses']:
            restList.append(nearby_restaurant)
    
    response = Response(json.dumps(restList),  mimetype='application/json')
    print(response) 
    return response

if __name__ == '__main__':
        app.run()