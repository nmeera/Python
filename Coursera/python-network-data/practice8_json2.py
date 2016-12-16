#Extracting json data from a string by using loop
import json

input1 = '''
[
  {"id" : "001",
   "x" : "2",
   "name" : "chuck"
  },
  {"id" : "009",
   "x" : "7",
   "name" : "Chuck"
  }
]'''

info = json.loads(input1)
print "User count: ", len(info)

for item in info: 
 print "Name: ",item["name"]
 print "Id: ", item["id"]
 print "Atttibute", item['x'] 
