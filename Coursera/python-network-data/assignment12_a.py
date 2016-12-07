# Scraping Numbers from HTML using BeautifulSoup 
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')

#for tag in tags:
 #      #Look at the parts of tag
#	print 'TAG: ',tag
#	print 'URL: ',tag.get('href', None)
#	print 'Contents:', tag.contents[0]
#	print 'Attrs: ',tag.attrs
#	print "\n\n"
sum1 = 0
for tag in tags:
#	print tag
#	print 'URL: ',tag.get('href', None)
	i = tag.contents[0]
	sum1 = sum1 + int(i)
print "total: ", sum1	
