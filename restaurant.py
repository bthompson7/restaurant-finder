'''
class to represent a resaurant 
'''

class Resaurant:
    def __init__(self,name,lat,lng):
        self.name = name
        self.lat = lat
        self.lng = lng
    
    def getName(self):
        return self.name

    def getLat(self):
        return self.lat

    def getLng(self):
        return self.lng