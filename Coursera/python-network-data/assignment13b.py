#####Calling a JSON API
## In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib
import json
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
 add = raw_input('Enter location: ') 
 if len(add) < 1 : brek

 url = serviceurl + urllib.urlencode({'sensor':'false', 'address': add})
 print 'Retrieving', url
 uh = urllib.urlopen(url)
 data = uh.read()
 print 'Retrieved',len(data),'characters'

 try: js = json.loads(str(data))
 except: js = None
 if 'status' not in js or js['status'] != 'OK':
  print '==== Failure To Retrieve ===='
  print data
  continue

 print json.dumps(js, indent=4)
 print "place_id: ", js["results"][0]["place_id"]
