# THIS PROGRAM DEFINE THE FACTORIAL FUNCTION USING ITERATION INSTEAD RECURSION. THIS ALLOWS US DO COMPUTATION THAT WORKING WITH RECURSION ARE LESS EFICIENT. AN EXAMPLE IS FACTORIAL FUNCTION. 

 
#THIS FUNCTION WAS MADE USING RECURSION. WITH THIS ONE WE HAD SOME PROBLEMS CALCULATING THE FACTORIAL OF NUMBER GREATEST THAN 900 


def factorialRec(n):
    if n==0:
	return 1
    else:
	return n * factorialRec(n-1) 


# THIS FUNCTION WAS MADE USING ITERATION. IN THAT SENSE THIS ONE IS BETTER BEACUSE CALCULATE THE DESIRED VALUE FOR NUMBERS GREATEST THAN 1000


def factorialIter(n):
     i=1
     while n>1:
	i*=n
	n-=1
     return i	


factorialIter(3)



# ANOTHER FIBONACCI FUNCTION DEFINITION. THIS ONE USE DICTIONARIES



previous = {0: 0, 1: 1}

def fibonacci(n):
    if previous.has_key(n):
        return previous[n]
    else:
        new_value = fibonacci(n-1) + fibonacci(n-2)		# THIS ONE USE RECURSION TO FIND THE FIBONACCI'S SUM
        previous[n] = new_value
        return new_value



