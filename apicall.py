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
DEFAULT_LOCATION = 'Gorham, ME'
SEARCH_LIMIT = 3

class YELP:
    def __init__(self):
        pass
    '''
    calls the yelp api 
    '''
    def search_api(api_key,term,location):
        data = "api call!"
        url_params = {
           'term': term.replace(' ', '+'),
            'location': location.replace(' ', '+'),
            'limit': SEARCH_LIMIT
        }
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
    return response.json()

