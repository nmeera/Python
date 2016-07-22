# This is for printing amax and min nunumbers  from user's input of "int" type
minimum = None
maximum = None

try:
    while True:
        inp = raw_input('Enter a number: ')
        if inp == 'done': 
            break
        num = int(inp)
    #   continue                            
        if minimum is None or num < minimum:
            minimum = num
        if maximum is None or num > maximum:
            maximum = num
except:
        print 'Invalid input'

print 'Maximum is:', maximum
print 'Minimum is:', minimum
