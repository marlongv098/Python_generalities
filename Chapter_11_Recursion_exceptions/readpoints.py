

"""
>>> num = readposint()
Please enter a positive integer: yes
yes is not a positive integer.  Try again.
Please enter a positive integer: 3.14
3.14 is not a positive integer.  Try again.
Please enter a positive integer: -6
-6 is not a positive integer.  Try again.
Please enter a positive integer: 42
>>> num
42
>>> num2 = readposint("Now enter another one: ")
Now enter another one: 31
>>> num2
31
>>>
"""

#def readpoints():			
   #if :
#   number=raw_input("Please enter a positive integer: ")	
   #else:
	#number=raw_input(argv[])	
#   try:
#	type(number)!=int or int(number) < 0 
	   #raise ValueError #('%s is not a positive integer, Try again.' % number) # print '%s is not a positive integer, Try again.' % number 	
   	
#   except ValueError:
#	print '%s is not a positive integer, Try again.' % number
#	number =  readpoints()
#   return number

#   try:
#	if type(number)==int and int(number) > 0:
#   	   return True	  
#   except:
#	print '%s is not a positive integer, Try again.' % number
#	#return False
#	number=readpoints()
#   return number
   #if number==True:
 #	return 
   #return True

#   num=readpoints()
#   while num==False:
#	readpoints()
#print number


def readposint(): 
    x = raw_input("Please enter a positive integer :")
    try:
        if (type(x)!=int) and (float(x)-int(x)> 0): raise(ValueError) 
    except:
        print x , "is not a positive integer.  Try again."
        return -1
    return x

y = readposint()
print y
while y == -1:
    readposint()

print y
#else:
#    'you have entered: ', y    

