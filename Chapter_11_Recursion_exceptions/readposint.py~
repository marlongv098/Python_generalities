

from sys import argv


def readposint(*args):			# IN THIS FUNCTION WE COULD USE IT WITH AND WITHOUT ARGUMENTS
	
    if len(args) == 0: 			# THIS LINE EVALUATES THE LEN OF THE ARGUMENTS TO DECIDE IF HAVE NOT GOT IT.	
	num=raw_input("Please enter the positive number: ")
    else :				# THIS LINE IS CHOSEN WHEN THE LEN OF ARGUMENTS IS GREATER THAN ONE. IN THIS CODE MUST BE 1.
	num=raw_input('%s' % args)

    try:					# THESE LINES ARE THE SOLUTION OF THE EXCEPTION PROBLEM,
	if ((type(num)!=int) and (int(num)<0)): raise(ValueError)	# WE HAVE TO BE CAREFULL WITH THIS CHUNK OF CODE DUE THIS LINE ALLOW US JUMP TO THE EXCEPTION. IF THIS LINE IS NOT WORKING WELL THE PROGRAM GAVE US A LOT OF PROBLEMS.
	
    except:
	print "%s is not a positive integer. Try again: " % num 	# THIS LINE PRINTS THE INFORMATION IN IT.  
	num=readposint()						# THIS LINE USE RECURSION TO START AGAIN THE PROGRAM.
    return int(num)							# THIS LINE CHANGE THE NUM RESULT INTO A INTEGER. THAT HAPPENED BECAUSE THE PROGRAM IS USING raw_input FUNCTION, THIS FUNCTION TRANSFORM THE RESULTS IN STRIGNS.
    	

# THESE ARE THE PROVES

#cat=readposint()
cat=readposint("Now enter another one: ")
print cat


# from readposint import *
