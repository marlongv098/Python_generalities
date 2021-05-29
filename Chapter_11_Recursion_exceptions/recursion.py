#### 	RECURSIVE FUNCTION TO NESTED SUM LIST AND TUPLES



def recursive_sum(nested_num_list):			# RECURSIVE FUNCTION TO SUM NESTED LIST AND TUPLES.
    sum = 0						# INITIALIZED THE SUM
    for element in nested_num_list:			# LINE TO EVALUATE NESTED LIST
        if type(element) == type([]):
            sum = sum + recursive_sum(element)		# RECURSION
	elif type(element)==type(()):			# LINE TO EVALUATE A NESTED TUPLE
	    sum = sum + recursive_sum(element)		# RECURSION
        else:
            sum = sum + element				# LINE TO CALCULATE THE SUM. AT THE END THIS IS THE LINE WHICH EVERYONE OF THE ELEMENT ARE GOING TO USE
    return sum



### RECURSIVE FUNCTION TO FIND THE LARGEST NUMBER INSIDE A LISTS, TUPLES OR COMBINATIONS OF BOTH



def recursive_max(nested_num_list):		
    """
      >>> recursive_max([2, 9, [1, 13], 8, 6])
      13
      >>> recursive_max([2, [[100, 7], 90], [1, 13], 8, 6])
      100
      >>> recursive_max([2, [[13, 7], 90], [1, 100], 8, 6])
      100
      >>> recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6])
      100
      >>> recursive_max((((13, 7), 90), 2, (1, 100), 8, 6))
      100
      >>> recursive_max((([13, 7], 90), 2, [1, 100], 8, 6))
      100
    """
    largest = nested_num_list[0]					# LINE THE FIND FIX THE FIRST LIST OR TUPLE ELEMENT
    while type(largest) == type([]) or type(largest) == type(()):	# IF THE FIRST ELEMENT IS A LIST OR TUPLE THIS LINE FIX THE FIRST ELEMENT OF THAT LIST OR TUPLE.
        largest = largest[0]				# TO FIX THIS LINE ASSIGN THE FIRST ELEMENT OF THE LARGEST ONLY IF IS A LIST OR TUPLE.

    for element in nested_num_list:			# THIS PASS TROUGH EVERY ELEMENT OF THE NESTED LIST OR TUPLE
        if type(element) == type([]):			# LINE TO EVALUATE THE LIST TYPE. 
            max_of_elem = recursive_max(element)	# FIX THE ELEMENT IN A RECURSIVE WAY 
            if largest < max_of_elem:			# COMPARE THE FIXED LARGEST WITH THE ELEMENTS OF THE LIST 
                largest = max_of_elem			# ASSING NEW VALUE TO THE LARGEST.
	elif type(element) == type(()):
	    max_of_elem = recursive_max(element)	# THESE LINES DO THE SAME ABOVE BUT IN A TUPLE TYPEL ELEMENT
	    if largest < max_of_elem:			
		largest = max_of_elem
        else:                           		# element is not a list 
            if largest < element:			# THIS CHUNK OF CODE WORK IN ELEMENT THAT THEY ARE NOT A LIST OR TUPLE
                largest = element

    return largest					# RETURN THE LARGEST NUMBER.


###############


def countdown(n):			# FUNCTION TO COUNT DOWN FROM 'n' TO 1 USING RECURSION. ANOTHER COPY OF THIS PROGRAM IS IN CHAPTER 6.THAT PROGRAM USE while  FUNCTION TO COUNT DOWN. 
    if n == 0:
        print "Blastoff!"
    else:
        print n
        countdown(n-1)			# RECURSION LINE.


def find_max(seq, max_so_far):		# THIS FUNCTION ONLY FIND THE LARGEST NUMBER IN A SEQUENCE. IT DID NOT CONSIDERED SUBSEQUENCES.
    if not seq:
        return max_so_far
    if max_so_far < seq[0]:				# LINE TO COMPARE THE MAX TO THE FIRST ELEMENT OF THE SEQUENCE. .
        return find_max(seq[1:], seq[0])		# LINE TO EVALUTATE THE NEXT ELEMENT OF THE SEQUENCE. THIS REPLACE THE FIRST MAX PUT IT IN THE FUNCTION
    else:
        return find_max(seq[1:], max_so_far)		# IF THE max_so_far > seq[0] THIS LINE REPLACE THE FIRST ELEMENT OF THE LIST. THIS PROCESS IN KNOWN SUCH AS EXHAUSTION.



def factorial(n):				# THE NEXT TWO, THE FACTORIAL AND FIBONACCI'S FUNCTIONS IT WAS DEFINED USING THE RECURSION METHOD BUT THE PROBLEM IN HERE IS THESE KIND OF METHOD IS NOT EFICIENT MAKING CALCULUS.
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci (n):				# THIS FUNCTIONS SPEND A LOT OF RESOURCES MAKING A SIMPLE CALCULUS
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)





if __name__ == '__main__':
    import doctest
    doctest.testmod()       
    
