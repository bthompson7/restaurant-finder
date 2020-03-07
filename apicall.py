'''
class for calling the yelp api
'''
import argparse
import json
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
SEARCH_LIMIT = 50

class Yelp:
    def __init__(self):
        pass

    '''
    calls the yelp api 
    '''
    def search_nearby(api_key,term,lat,lng):
        data = "api call!"
        url_params = {
           'term': term.replace(' ', '+'),
            'latitude':lat,
            'longitude':lng,
            'open_now':True,
            'limit': SEARCH_LIMIT
        }
        print(url_params)
        return find(API_HOST, SEARCH_PATH, api_key, url_params=url_params)

    def search_by_id(api_key,id):
        restDetailsData = "api call2"
        BUSINESS_PATH = '/v3/businesses/'
        BUSINESS_PATH+= id
        return find(API_HOST, BUSINESS_PATH, api_key, url_params=id)

'''
helper function
'''
def find(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    print(u'Querying {0} ...'.format(url))
    response = requests.request('GET', url, headers=headers, params=url_params)
    response_code = response.status_code
    if response_code == 200:
        print("response ok %s"%response_code)
    else:
        print("ERROR!: %s"%response_code)
    return response.json()

