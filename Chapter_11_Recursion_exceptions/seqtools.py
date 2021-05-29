# TUPLES AND PURE FUNCTION MODIFIERS
#
# seqtools.py
#
import string

def swap(x, y):			# THIS IS A TUPLE FUNCTION
    return y, x


def insert_in_middlelist(val, lst):
    middle = len(lst)/2			# THIS IS THE MIDDLE OF THE LIST
    lst[middle:middle] = [val]		# THIS NOTATION ALLOW US TO PUT AN ELEMENT INSIDE A LIST WITHOUT BRACKETS. IF I USE THE 'lst[middle]=[val]' NOTATION. THIS ONE PUT A LIST INSIDE THE LIST. ALSO I COULD PUT HERE AND A RETURN FUNCTION THIS TO SHOW US THE OUTPUT.
    return lst


def insert_in_middletuple(val, tup):
    middle = len(tup)/2			# THIS IS THE MIDDLE OF THE TUPLE
    return tup[:middle] + (val,) + tup[middle:]		# HERE WE ARE MAKING THE NEW TUPLE. THE FIRST PART OF THE NEW TUPLE ARE THE FIRST ELEMENTS OF THE OLD TUPLE AFTER THAT WE INTRODUCE THE NEW ELEMENT IN THE TUPLE FOLLOWED BY A COMMA AFTER THAT WE PUT THE LAS ELEMENTS OF THE OLD TUPLE. THAT IS ALL.


# GENERAL INSERT IN THE MIDDLE. WORKS FOR EVERY ELEMENT DESCRIBED BELOW
# LIST
# STRING
# TUPLE


def encapsulate(val, seq):
    if type(seq) == type(""):		# HERE EVALUATES IF seq  IS A STRING
        return str(val)			# REPLACE THE VALUE IN THE STRING
    if type(seq) == type([]):		# HERE EVALUATES IF seq IS A LIST
        return [val]			# REPLACE THE VALIE IN THE LIST
    return (val,)			# HERE EVALUATES IF seq IS A TUPLE AND REPLACE. THIS IS THE 'else' EQUIVALENCY 


def insert_in_middle(val, seq):		# THIS FUNCTION INSERT THE VALUE IN THE MIDDLE OF ANYONE OF THE FOLLOWING: STRING, TUPLE OR LIST 
    middle = len(seq)/2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]		# JOIN THE NEW ELEMENT TO THE OLD ONE. WORK FOR EVERY CASE OF STUDY. STRING, TUPLE, LIST.


def make_empty(seq):
    """
    >>> make_empty([1, 2, 3, 4])
    []
    >>> make_empty(('a', 'b', 'c'))
    ()
    >>> make_empty("No, not me!")
    ''
    """
    if type(seq)==type(''):
	return ''
    if type(seq)==type(()):
	return ()
    return []



def insert_at_end(val, seq):
    """
      >>> insert_at_end(5, [1, 3, 4, 6])
      [1, 3, 4, 6, 5]
      >>> insert_at_end('x', 'abc')
      'abcx'
      >>> insert_at_end(5, (1, 3, 4, 6))
      (1, 3, 4, 6, 5)
    """
    if type(seq)==type(''):
	return seq + val
    if type(seq)==type(()):
	return seq[0:] + (val,) 
    return seq[:]+ [val]



def insert_in_front(val, seq):
    """
      >>> insert_in_front(5, [1, 3, 4, 6])
      [5, 1, 3, 4, 6]
      >>> insert_in_front(5, (1, 3, 4, 6))
      (5, 1, 3, 4, 6)
      >>> insert_in_front('x', 'abc')
      'xabc'
    """
    if type(seq)==type(''):
	return val + seq
    if type(seq)==type(()):
	return (val,) + seq[0:]
    return [val] + seq[:]



def index_of(val, seq, start=0):
    """
      >>> index_of(9, [1, 7, 11, 9, 10])
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
      6
      >>> index_of('y', 'happy birthday')
      4
      >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
      1
      >>> index_of(5, [2, 3, 4])
      -1
      >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
      -1
    """
    try:
         index_element=seq.index(val)		# THIS CHUNK WORKS SO WELL ONLY HAVE PROBLEMS WITH THE THIRD DOCTEST
         return index_element
    except ValueError:
            return -1

    #for i, j in enumerate(seq):		# THIS ONE WORKS BUT HAVE PROBEM WITH THE -1 RETURN AN ALSO WITH THE THIRD DOCTEST
	#if j==val:
	 # return i

    #for i in range(len(seq)):
	#if seq[i] == val:
	 # return i
	#return -1
	  
    if type(seq)==type(''):			# THE CHUNKS OF PROGRAM BELOW WORKS THE PROBLEM IS -1 RETURN AND THE THIRD DOCTEST.
	for i in range(len(seq)):
	   if seq[i]==val:
		start=i				# I MUST TO SAID THAT ALSO IN MANY OF THE CASES A DO NOT USE THE START ELEMENT OF THE FUNCTION.
#		return start
	   #else:
		#if seq[i]!=val:
		 # start=-1
		  #return start
    if type(seq)==type([]):
	for i in range(len(seq)):
	   if seq[i]==val:
		start=i
#		return start
	   #else:
		#if seq[i]!=val:
		 # start=-1
		  #return start
    else:
	for i in range(len(seq)):
	   if seq[i]==val:
		start=i
#		return start			# THE CHUNKS OF THIS PROGRAM FINISH HERE. STILL HAVE THE SAME PROBLEMS. THE BEST OF THE PROGRAM IS TEH FRIST ONE ABOVE
 	   #else:
		#if seq[i:]!=val:
		 # start=-1
		  #return start


def remove_at(index, seq):				# IN THIS FUNCTION WE HAVE TO MAKE DIFFERENT CHUNK OF CODE FOR EACH ONE WAS THINKED TO WORK WITH STRING, TUPLE OR LIST
    """
      >>> remove_at(3, [1, 7, 11, 9, 10])
      [1, 7, 11, 10]
      >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
      (1, 4, 6, 7, 0, 3, 5)
      >>> remove_at(2, "Yomrktown")
      'Yorktown'
    """							
    if type(seq)==type([]):				# IN THIS CHUNK OF PROGRAM WE ARE WORKING WITH LISTS
    	del seq[index]	
        return seq 
    if type(seq)==type(()):				# IN THIS CHUNK OF PROGRAM WE ARE WORKING WITH TUPLES
	return seq[:index] + seq[index+1:]		
    if type(seq)==type(''):				# AND HERE WE ARE WORKING WITH STRINGS
	seq= seq.replace(seq[index],'')			
	return seq					# THE BEST OF THIS KIND OF PROGRAMS IS WE HAVE TO REMENBER CONCEPTS OF DIFFERENTS PYTHON CODE RULES. 
	


def remove_val(val, seq):		# HERE I DO NOT HAVE MANY PROBLEMS WITH THE CODE DUE THE DOCTEST CASE ONLY CONSIDER TUPLES AND LIST. IF THE DOCTEST IT WILL BE CONSIDER STRINGS THIS SOLITUON IS NOT OPTIMS
    """
      >>> remove_val(11, [1, 7, 11, 9, 10])
      [1, 7, 9, 10]
      >>> remove_val(15, (1, 15, 11, 4, 9))
      (1, 11, 4, 9)
      >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
      ('who', 'when', 'where', 'why', 'how')
    """
    if type(seq)==type([]):				# IN THIS CHUNK OF PROGRAM WE ARE WORKING WITH LISTS
    	for i in range(len(seq)):
	    if seq[i]==val:
		del seq[i]				# HERE WE DELETE THE ELEMENT WHICH PROVE THE STATEMENT CONDITION.
		return seq
    if type(seq)==type(()):				# IN THIS CHUNK OF PROGRAM WE ARE WORKING WITH TUPLES
	seq=list(seq)
	remove_val(val,seq)				# WE ARE USING RECURSION
	seq=tuple(seq)
	return seq

        #if type(seq)==type(''):				# AND HERE WE ARE WORKING WITH STRINGS. HERE THIS ONE WAS NOT NECESSARY.
	#seq= seq.replace(seq[index],'')			
	#return seq					# THE BEST OF THIS KIND OF PROGRAMS IS WE HAVE TO REMENBER CONCEPTS OF DIFFERENTS PYTHON CODE RULES.  
	#seq=list(seq)
	#a=remove_at(index, seq)
	#return a.join()
	#return str(a)



def remove_all(val, seq):		# FUNTION TO REMOVE ELEMENT IN A LIST A STRING. IN THE TUPLE CASE IS ONLY NECESSARY USE RECURSION CHANGING TUPLE BY A LIST. THE SAME METHOD USED IN 'remove_val'	
    """
      >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
      [1, 7, 9, 10, 2]
      >>> remove_all('i', 'Mississippi')
      'Msssspp'
    """
    if type(seq)==type([]):		# EVALUATE IF IS A LIST
      h=[]				# THIS LINE MAKE MEMORY SPACE TO STORE THE NEW LIST
      for i in range(len(seq)):
	if seq[i]!=val:			# CONDITION. WE HAVE TO REMOVE EVERY SAME ELEMENT IN THE LIST 
	  h+=[seq[i]]			# LINE TO STORE THE NEW LIST
      return h

    if type(seq)==type(''):
      seq=seq.replace(val,'')		# HERE WE ONLY USE THE STRING MODULE
      return seq



def count(val, seq):			# THIS FUNCTION COUNT THE ELEMENTS SAME ELEMENTS IN A LIST, TUPLE, A COMBINATION OF THEM AND A STRING.
    """
      >>> count(5, (1, 5, 3, 7, 5, 8, 5))
      3
      >>> count('s', 'Mississippi')
      4
      >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
      2
    """
    if type(seq)==type(()):		# FOR THE TUPLE CASE WE COUNT EACH ONE OF THE ELEMENTS.
      h=0				# MAKE SPACE TO STORE THE COUNT
      for i in range(len(seq)):
	if seq[i]==val:			# CONDITION
	  h+=1				# COUNT THE ELEMENTS
      return h

    if type(seq)==type([]):		# FOR THE LIST OPTION. IN THIS CASE WE CHANGE THE LIST AND TUPLE BY A STRING AND USED RECURSION TO CALCULE THE AMOUNT OF ELEMENTS 
      seq=str(seq)			# CHANGING seq TO A STRING TYPE
      val=str(val)			# CHANGING val TO A STRING TYPE 
      count(val,seq)			# HERE WE ARE USING RECURSION
      #return seq	

    if type(seq)==type(''): 
      return seq.count(val)		# COUNT IS A STRING FUNCTION TO COUNT THE AMOUTN OF val IN THE STRING seq


def reverse(seq):			# CALCULATES THE REVERSE OF A STRING TUPLE OR STRING IN ONE LINE.
    """
      >>> reverse([1, 2, 3, 4, 5])
      [5, 4, 3, 2, 1]
      >>> reverse(('shoe', 'my', 'buckle', 2, 1))
      (1, 2, 'buckle', 'my', 'shoe')
      >>> reverse('Python')
      'nohtyP'
    """
    return seq[::-1]			# THE REVERSE PYTHON FUNCTION WORKS WELL TO LIST, TUPLES AND STRINGS. THE CHUNKS OF PROGRAMMS BELOW DO THE SAME BUT THIS IS BETTER.


#    if type(seq)==type([]):		# LIST TYPE 
#	return seq[::-1] 		# THIS LINE REVERSE THE LIST.
    
#    if type(seq)==type(()):
#	seq=tuple(reverse(list(seq))) 	    # HERE WE ARE USING RECURSION TO CALCULATE THE TUPLE REVERSE. CHANGING THE TUPLE BY A LIST AND VICEVERSA
#	return seq

#    if type(seq)==type(''):		
#	return seq[::-1]		# HERE WE DID THE SAME THAT THE LIST TYPE. THE ONLY DIFERENCE IS IN THIS ONE WE DID NOT CHANGE THE STR BY A LIST. PYTHON RECOGNIZE THE SAME COMAND IN BOTH LIST AND STRING. 



def sort_sequence(seq):
    """
      >>> sort_sequence([3, 4, 6, 7, 8, 2])
      [2, 3, 4, 6, 7, 8]
      >>> sort_sequence((3, 4, 6, 7, 8, 2))
      (2, 3, 4, 6, 7, 8)
      >>> sort_sequence("nothappy")
      'ahnoppty'
    """
    if type(seq)==type([]):			# LIST TYPE 
	return sorted(seq)			# ONE OF THE PYTHON FUNCTIONS TO SORT A LIST.
    
    if type(seq)==type(()):
	seq=tuple(sort_sequence(list(seq)))	# HERE WE USE RECURSION TO TUPLES SORT 
	return seq
	
    if type(seq)==type(''):
	a=''	
	return a.join(sorted(seq))		# I MUST PRACTICE THE join FUNCTION BECAUSE I DO NOT KNOW HOW IT WORKS. IN THIS CASE a IS THE STRING SPACE MADE TO STORE THE NEW STRING  
      



if __name__ == '__main__':
    import doctest
    doctest.testmod()       
