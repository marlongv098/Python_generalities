#
# infinite_recursion.py
#



def recursion_depth(number):				# THIS IS A BASIC INFINITE RECURSION FUNCTION. PRINTS AN ERROR FROM PYTHON SHELL.WHEN THE FUCNTION EXCEDED THE ALLOWED AMOUNT OF ELEMENTS.
    print "Recursion depth number %d." % number
    recursion_depth(number + 1)				# THIS LINE COUNT THE AMOUNT OF ELEMENTS.

#recursion_depth(0)



def recursion_depth(number):
    print "Recursion depth number %d." % number
    try:
        recursion_depth(number + 1)
    except:
        print "Maximum recursion depth exceeded."

recursion_depth(0)

