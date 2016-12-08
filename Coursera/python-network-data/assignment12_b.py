#Following Links in Python (link in link) 
import urllib
from BeautifulSoup import *

#url = raw_input('Enter URL: ')
#url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
url  = "http://python-data.dr-chuck.net/known_by_Kearney.html"
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)
#tags = soup('a') # Retrieve all of the anchor tags
#for tag in tags:
 #      #Look at the parts of tag
#	print 'TAG: ',tag
#	print 'URL: ',tag.get('href', None)
#	print 'Contents:', tag.contents[0]
#	print 'Attrs: ',tag.attrs
#	print "\n\n"
p = raw_input("Enter the position: ")
r = raw_input("How many time it should repate:  ") 
k = 0
while True:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a') # Retrieve all of the anchor tags
	k = k + 1
#	if k >= int(r): print "CALLING BREAK>>!!  "; break
	c = 0
	for tag in tags:
		c = c + 1
		if c == int(p) :
			url = tag.get('href', None) ;print url
			y = tag.contents[0] ;print y
	print k,c,int(r)
	if k >= int(r): print "CALLING BREAK>>!!  "; break
print url , y

