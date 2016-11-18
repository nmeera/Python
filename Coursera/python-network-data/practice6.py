#The repeat characters (* and + )push outward in both  directions (greedy) to matchthe largest possible string.

import re 

x = 'From: Using the : character'
y = re.findall('^F.+:',x) # greedy matching
print y

print "<<---------------------------->>"

#Not all regular expression repeat codes are greedy! if you add a '?' character - the + and * chill out a bit..

x = 'From: Using the : character'
y = re.findall('^F.+?:',x) # greedy matching
print y
