import unittest,os,sys,json
sys.path.append('/home/ben/restaurant-app')
from apicall import Yelp

class TestAPICall(unittest.TestCase):
    def test_search_by_id(self):
        api = Yelp
        dataFromApi = api.search_by_id('_L1U_nqs_te4a9-oH17BoQ')

    def test_search_by_cat(self): 
        api = Yelp
        dataFromApi = api.search_nearby_for_type(2,43.8424131,-70.623781,'comfortfood')
        print(dataFromApi)
        


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True



if __name__ == '__main__':
    unittest.main()