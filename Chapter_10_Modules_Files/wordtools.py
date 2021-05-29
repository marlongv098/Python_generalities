import string


def cleanword(word):	# THIS FUNCTION CLEAN THE WORD IN THE FUNCTION. IT THE THE STRING AND REMOVE THE CARACTERS ON IT.
    """
    >>> cleanword('what?')
    'what'
    >>> cleanword('"now!"')
    'now'
    >>> cleanword('?+="word!,@$()"')
    'word'
    """
    s=''		# THIS WAS THE FIRST IDEA. THE PROBLEM WAS I WAS USING "replace" STRING FUNCTION ON IT.  
    for i in word:
      if i in '!",@$+=?()': 
         i=''			# HERE ONLY REPLACE THE CARACTERS ON THE STRING.
      s+=i			# HERE WE JOIN AGAIN THE STRING WITHOUT ANY CONSIDERING CARACTERS. 
    return s

#    for i in word:
#        if i in '!",@$+=?':
#    	   s=word.replace(i,'')		# I CAN NOT USE 'replace' STRING FUNCTION IN THIS EXERCISE BECAUSE THAT FUNCTION ONLY REPLACE ONE CARACTER OF THE SET OF CARACTERS.
#    return s	

    #s=word.replace('!",@$+=?','')
    #return s

   
def has_dashdash(s):
    """
    >>> has_dashdash('distance--but')
    True
    >>> has_dashdash('several')
    False
    >>> has_dashdash('critters')
    False
    >>> has_dashdash('spoke--fancy')
    True
    >>> has_dashdash('yo-yo')
    False
    """
    if '--' in s:		# THE SOLUTION WAS IMPLEMENTED SO EASY. ONLY WAS NECESSARY FIND THE SUBSTRING INSIDE THE STRING..
	return True
    else:
	return False

#    for i in s:		# IN THIS CHUNK OF PROGRAM I WAS TRYING TO FIND THE DASH CARACTER INSIDE THE STRING, ONCE THE CARACTER WAS FOUND THE IDEA WAS USED THAT POSSITION (THE NUMBER 'a') TO RETURN THE True OR False. 
#	a=s.find('-')
#	if i==s[a]: #and i+1==s[a]:	# THIS CHUNK DOES NOT WORKS.
#	   return True	
#	else:
#	   return False


def extract_words(s):
    """
    >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
    ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
    >>> extract_words('she tried to curtsey as she spoke--fancy')
    ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """
    s=s.lower()			# THIS FIRST STEP IS TAKE THE STRING AND CHANGE TO LOWER LETTERS
    c=''			# MAKE THE SPACE TO STORE OUR RESULT
    if '--' in s:		# EVALUATE THE DASH DASH SUBSTRING IN THE STRING
	c=s.replace('--',' ')
        a=c.split()		# THE LINE ABOVE REPLACE AND THIS ONE SPLIT THE STRING TO GET THE RESULT
        return a
    else:
        for i in s:		# HERE I USE THE SAME IDEA OF THE CHUNK OF CODE INITIALY USED. 
	  if i in ',".!?':
    	   i=''
	  c+=i
	  a=c.split()
	return a

    #b=['' for x in range(len(a))]	# IN THIS CHUNK OF PROGRAM I WAS TRYING TO RESOLVE THE EXERCISE. THE PROBLEM WITH THIS CHUNK OF CODE WAS THE SECOND ONE LINE OF HTE DOCTEST TO BE EXACT THE '--' DASH DASH ASIGMENT IN THE STRING.
#    for i in range(len(a)):
	#if '--' in a[i]:		# THIS DOES WORK WELL BUT THE IDEA WAS NOT BAD AT ALL. THE ONLY PROBLEM WAS THAT CHUNK IT WAS INSIDE THE FOR LOOP.
	   #a[i].replace('--,' ')
#	for j in a[i]:			# THIS CHUNK RESOLVED THE FRIST ONE DOCTEST ASSIGMENT.
#	   if j in ',".!?':
#    	      j=''
# 	   b[i]+=j
    #return b


#    a=a.split()			# THE FOLLOWING CHUNK OF CODES WERE THE FIRST PROVES.
#    for i in range(len(a)):
#	a[i]=a[i].lowercase()
#    a=''
#    a=s.lowercase()
    
    #return a		

#    for i in a:
#       if i in '-"':	
#	 i=''
#       a+=i
#    return a


def wordcount(word, wordlist):
    """
    >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['now', 2]
    >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
    ['is', 4]
    >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['time', 1]
    >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['frog', 0]
    """
    #s=[]
    #for i in range(len(wordlist)):
    a=wordlist.count(word)		# HERE ONLY WAS NECCESARY USE THE 'count' STRING FUNTION TO RESOLVE THE PROBLEM.
    return [word,a]	


def wordset(wordlist):
    """
    >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['is', 'now', 'time']
    >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
    ['I', 'a', 'am', 'is']
    >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
    ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    wordlist=dict.fromkeys(wordlist)		# THIS LINE GENERATES A LIST DICTIONARY. EACH KEY IT WAS STORE IN THE LIST 'wordlist'.
    wordlist=wordlist.keys()			# HERE WE OBTAINED THE KEYS OF THE STORE DICTIONARY THAT WE WAVE CREATED..
    wordlist.sort()				# HERE WE ARE SORTING THE OBTAINED "wordlist"
    return wordlist


#    for i in range(len(wordlist)):		# ON THE CHUNK OF PROGRAM BELOW I WAS RESOLVING THE PROBLEM COUNTING THE LIST POSITIONS AND TRYING TO REPLACED BUT I CAN NOT DO IT SO WELL.
#	if wordlist[i]==wordlist[i+1]:		# LOOK UP LATER
#    	  a=wordlist.remove(wordlist[i+1])
#    b=['' for x in range(len(wordlist))]  	# IS IS NOT NECCESARY 
    
#    w=list(set(wordlist))

#    for i in range(len(wordlist)):
#	if wordlist[i]==wordlist[i+1]:
#		w=wordlist.remove(wordlist[i])   # HERE I WAS TRYING TO REMOVE THE SAME LIST ENTRIES.
#		return w

#	j=range(1,len(wordlist))
#	if i < j and j <= len(wordlist):
#         for j in range(i,len(wordlist)):
#	  if wordlist[i]==wordlist[j]:
#		b=wordlist.remove(wordlist[j])
#	return b


def longestword(wordset):
    """
    >>> longestword(['a', 'apple', 'pear', 'grape'])
    5
    >>> longestword(['a', 'am', 'I', 'be'])
    2
    >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
    34
    """
    r=""			# THIS WAY IS EASY TO UNDERSTAND THE PROBLEM. THIS IS USED TO STORE THE RESULT
    for i in wordset:		# HERE WE ARE ENUMERATING THE LIST ELEMENTS
	if len(i) > len(r):	# HERE ME COMPARE THE LIST ELEMENTS. IN THE FIRST STAGE ME ARE COMPARING THE FIRST STAGE OF THE LIST WITH A ZERO LEN LIST.
	   r=i  		# WHEN WE FIND A BIGGER ELEMENT STORE THAT ELEMENT IN THE EMPTY POSITION 'r'  
    return len(r)		# AFTER PASS THROUGH THE LIST WE PRINT THE RESULT
    

    max(wordset)		# I DO NOT KNOW THIS FUNCTION DOES NOT WORKS WELL IN A LIST

#	if 
#    for i in range(len(i)):
#	wordset.count(wordset[i])
	


if __name__ == '__main__':
    import doctest
    doctest.testmod()
