import string 

def rever_func(n):		# I DO NOT KNOW WHY THIS DOES NOT WORK.
	print n[::-1]


def reverse(s):		# THIS FUNCTION REVERSE A STRING.
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    return s[::-1]    	# IT DOES NOT WORK WITH THE FUNCTION "rever_func"


def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
    """
    return "%s%s" % (s[::], s[::-1])


def remove_lett(letter,strng):		# THE ONLY PROBLEM WITH THIS FUNCTION ARE THE "" QUOTES. THE PROGRAM PRINT THE SOLUTION WITHOUT THE QUOTES.  
	for let in strng:
	  if let==letter:
	    strng=strng.replace(let, "") 
	    
	print '%s' % strng


def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    return strng.replace(letter,"")
    #return remove_lett(letter, strng)


def palindrome(s):
	if s==s[::-1]:
	  print True
	else:
	  print False


def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """
    return palindrome(s)


def count_silables(sub, s):		# IN THIS FUNCTION I WAS TRYING TO COUNT THE STRING AMOUNT INSIDE ANOTHER STRING. I COULD DO IT BUT I STILL HAVING THE SAME PROBLEM WITH THE "ana" STRING IN THE STRING "banana" THERE IS TW0 BUT THE THE PROGRAM COUNT ONLY ONE..
	count=0
	j=len(sub)
	for i in range(len(s)):
	  if s[i:i+j] == sub:
	        count=s.count(sub)	
	print count
	 

def count(sub, s):	# AFTER MANY PROVES THE BEST WAY TO DO IT WAS USING THE STRING MODULE.
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    #return s.count(sub,0,len(str(s))) 		# IT HAPPENDS THE SAME WITH THE COUNT FUNCTION IN STRING.MODULE.
    return count_silables(sub, s)	

def remove_lett_group(sub, s):
	s=s.find(sub)
	s.replace(sub)
	print s
	#if sub in s:
	  	#=s.replace(sub,"")	
	#print s
	#for let in s:
	#for l in sub:
	#    s=s.replace(l, "") 
	#print '%s' % (s)

def remove(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    return remove_lett_group(sub,s)			# THIS 
    #return s.replace(sub,"")


def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    return s.replace(sub,"")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

