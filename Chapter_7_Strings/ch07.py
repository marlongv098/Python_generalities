

def prefix_fun():		# THIS PROGRAM FIX THE PROBLEM IN SOME OF THE PREFIXES. EXACTLY "O" AND "Q".
	prefixes="JKLMOPQ"	 
	suffix="ack"
	for n in prefixes:
	  if n=="J" or n=="K" or n=="L" or n=="M" or n=="P":
	    print n + suffix
	  else:
	    print n + "u" +suffix

#prefix_fun()


def count_letters(n,l):		# THIS FUNCTION WAS MADE TO COUNT THE AMOUNT OS SAME ELEMENTS IN A STRING. THE CHOSEN ONE ELEMENT IS AN ARGUMENT.
	count = 0
	for char in str(n):
	    if char == l:
	        count += 1
	print count

#cat=raw_input("what do you want?: ")
#bet=raw_input("which letter would you like count ")
#counting_looping_string(cat, bet)

def count_letter_find(strng, ch, start=0):	# THIS PROGRAM FIND AND COUNT LETTER OR CARACTER IN A STRING USING A COUNTER. THE START ARGUMENT ALLOW US BEGIN IN A DIFFERENT POSITION OF THE STRING.
    index = start
    while index < len(strng):
        if strng[index] == ch:
            print index
        index += 1
    return -1

#cat=raw_input("write the string: ")
#bet=raw_input("which letter would you like count: ")
#dot=input("write the begin position to search: ")
#count_letter_find(cat, bet, dot)


def rever_func(n):
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


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_without_vowels =''
    for letter in vowels:
        if letter not in vowels:
            s_without_vowels += letter
    return s_without_vowels


def remove(n):
	"""
	>>> remove('asjdi')
	sjdi
	>>> remove('aeihfgr')
	hfgr
	"""
	return remove_vowels(n)

#cat=raw_input("write the string ")
#remove_vowels(cat)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""
>>> "%s %d %f" % (5, 5, 5)
'5 5 5.000000'
>>> "%-.2f" % 3
'3.00'
>>> "%-10.2f%-10.2f" % (7, 1.0/2)	# IN THIS LINE THE MINUS INDICATES THE DIRECTION OF THE SPACES BETWEEN EACH NUMBER. THE NUMBER NEXT TO IT THE AMOUNT OF SPACES BETWEEN NUMBERS. AND THE NUMBER AFTER THE POINT INDICATES THE QUANTITY OF FLOATING POINTS FOR EACH NUMBER.
'7.00      0.50      '
>>> print "$%5.2fn $%5.2fn $%5.2f" % (3, 4.5, 11.2)
$ 3.00n $ 4.50n $11.20


>>> "%s %s %s" % ("this", "that", "something")
'this that something'
>>> "%s %s %s %s" % ("yes", "no", "up", "down")
'yes no up down'
>>> "%d %f %s" % (3, 3, "three")
'3 3.000000 three'
>>> "%d %d %s" % (3, 3, "three")
'3 3 three'
>>> "%d %.2f %s" % (3, 3, "three")
'3 3.00 three

"""


