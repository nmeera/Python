# This pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common, that there is a method called get() that does this for us
# We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one.


count = dict()
names = ['meera','mujeer','sridhar','meera','meera','boss','sridhar','karteek']
for name in names:
#	if  name not in count:
#		count[name]=1
#	else:
#		count[name] =  count[name] + 1
	count[name] = count.get(name,0)+1 #By using this get() method we can skip above 4 lines code 

print count
