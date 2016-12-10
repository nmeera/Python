# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file and enter the sum, 

import urllib
import xml.etree.ElementTree as ET

url  = raw_input('Enter the URL: ')
data = urllib.urlopen(url).read()
tree = 	ET.fromstring(data)

son = 0			## We can use anyone method of below ##
############################# First method ################################################
lst =  tree.findall('comments/comment') #Here we get list of elements
#print lst[0].find('count').text  # like this we can retrive value/text off count in list of particular item in List
for item in lst:
	i = item.find('count').text 
	son = son + int(i)

############################## Second method  ##############################################
#lst =  tree.findall('.//count') ## Here './/count' is equal to 'comments/comment/count'
#for i in lst:
#	son = son + int(i.text)

print "Sum of numbers: ",son
