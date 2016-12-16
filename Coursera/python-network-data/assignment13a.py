#Extracting Data from JSON
# use this url http://python-data.dr-chuck.net/comments_298997.json
import urllib
import json

url1 = raw_input('Enter the URL: ')
url2 = urllib.urlopen(url1).read()
info = json.loads(str(url2))
sum1=0
i = 0
try:
 while True:
#  print info['comments'][i]["count"]
  sum1 = sum1 + info['comments'][i]["count"]
  i = i + 1
except:
 print "list range completed or out of range"

print "sum: ", sum1
