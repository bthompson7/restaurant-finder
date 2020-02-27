'''
class for calling the yelp api

Client ID: ItgnlXYQLsD3_6xF47TJuQ
API Key

tn0G7Fq-F_RSxsvFfiYZ-8yBnuYP8xx58hzTr-kfCPILYlXHC-fvNvBccNJ_IOYfvvDJcHxFy_8eF8uRJxqPTXpnGeRH5Pl5UJAdNm-CykfdKW98Wpw-aOWEYr9NXnYx


'''
from __future__ import print_function
import argparse
import json
import pprint
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

DEFAULT_TERM = 'dinner'
SEARCH_LIMIT = 45

class Yelp:
    def __init__(self):
        pass

    '''
    calls the yelp api 
    '''
    def search(api_key,term,lat,lng):
        data = "api call!"
        url_params = {
           'term': term.replace(' ', '+'),
            'latitude':lat,
            'longitude':lng,
            'limit': SEARCH_LIMIT
        }
        print(url_params)
        return find(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


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
    print(response)
    return response.json()

