#Exercise 5: More Variables and Printing

name = 'Pathan'
age = 35 #not a lie
height = 180 #cm's
weight = 82 #kg's
eyes = 'Blue'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s" %name
print "He's %d cm's tall" %height
print "He's %d kg's heavy" %weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" %(eyes,hair)
print "His teeth are usally %s depending on the tea" %teeth

#this line is tricky,try to get it exactly right

print " If I add %d, %d, and %d I get %d. " % (age,height,weight,age + height + weight) 

