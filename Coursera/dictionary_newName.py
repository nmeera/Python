#When we encounter a new name, we need to add a new entry in the dictionary and if this the second or later time we have seen the name, we simply add one to the count in the dictionary under that name

count = dict()
names = ['meera','mujeer','sridhar','meera','meera','boss','sridhar','karteek']
for name in names:
	if  name not in count:
		count[name]=1
	else:
		count[name] =  count[name] + 1

print names

print count
