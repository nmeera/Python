# Matching and Extracting data
#When we use re.findall(), it returns a list of zeros or more sub-strings that match the regex. 
import re 

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # see the difference of '+' with &with out 
print y

y  = re.findall('[AEIOU]', x)
print y

y  = re.findall('[aeiou]+', x)
print y
