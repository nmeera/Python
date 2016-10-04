print '\nWhat\'s your name Mr.?',
name = raw_input(' ')

print '\nHow old are you, Mr. %s ?' %name,
age = int(raw_input())

print '\nHow tall are you (in cms), Mr. %s ?' %name,
height = int(raw_input())

print '\nHow much you weigh(in kgs), Mr %s ?' %name,
weight = int(raw_input())

print '\nSo, Mr. %s is %d years old, %d cms tall and %d kgs weight' %(name,age,height,weight)
