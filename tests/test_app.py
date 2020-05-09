import unittest,os,sys,json,requests
sys.path.append('/home/ben/restaurant-app')
from apicall import Yelp

class TestApp(unittest.TestCase):
    def test_getData(self):
        data =  {
	"location": {
		"lat": 43.740220699999995,
		"lng": -70.4526554
	}
}
        url = 'https://findarestaurantnearme.herokuapp.com/findlocation'
        x = requests.post(url, data = data)
        print(x.status_code)
        self.assertEqual(x.status_code,200)


if __name__ == '__main__':
    unittest.main()