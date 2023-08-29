import requests
import json

api_url = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"
response = requests.get(api_url)
print( response.ok )

_cars = response.json()
cars = _cars.get( "Results")
for car in cars:
    print( car )

class Cars :
    def __init__ (self, makeid, name ) :
        self.makeid = makeid
        self.name = name

