# Scraping Numbers from HTML using BeautifulSoup 
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

#for tag in tags:
#        #Look at the parts of tag
#	print 'TAG: ',tag
#	print 'URL: ',tag.get('href', None)
#	print 'Contents:', tag.contents[0]
#	print 'Attrs: ',tag.attrs
#	print "\n\n"

for i in tags:
	print i
