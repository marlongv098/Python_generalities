

def compare(a, b):	# THE PROBLEM OF THE COMPARE FUNCTION IS THE SECOND ONE AND THE LAST ONE, THAT ONES DO NOT PASS DE TEST BECAUSE THE FUNCTION IS EXPECTING NUMBERS BUT THEY GAVE A BOOLEAN RETURN (TRUE AND FALSE) 
    """
      >>> compare(5, 4)   
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 3)
      -1
    """
    return a>b or a==b #and a<b

def is_factor(f, n):		# THIS FUNCTION TELL US IF ONE NUMBER IS FACTOR OF THE ANOTHER.
    """
      >>> is_factor(3, 12)
      True
      >>> is_factor(5, 12)
      False
      >>> is_factor(7, 14)
      True
      >>> is_factor(2, 14)
      True
      >>> is_factor(7, 15)
      False
    """
    return n % f==0

def is_multiple(m, n):  		# THIS FUNCTION CALCULATES THE MULTIPLE OF A NUMBER
    """
      >>> is_multiple(12, 3)
      True
      >>> is_multiple(12, 4)
      True
      >>> is_multiple(12, 5)
      False
      >>> is_multiple(12, 6)
      True
      >>> is_multiple(12, 7)
      False
    """
    return m%n==0


def f2c(t):		# THIS FUNCTION CONVERT FARENHEIT TO CELCIUS.SOME OF THE PROBLEMS I HAD WAS THE FLOATING POINT. i FIXED ADDING A ZERO IN THE RESULTS AND SOME ITEMS OF TEMPERATURE.. 
    """
      >>> f2c(212)
      100.0
      >>> f2c(32)
      0.0
      >>> f2c(-40)
      -40.0
      >>> f2c(36)
      2.0
      >>> f2c(37.0)
      3.0
      >>> f2c(38)
      3.0
      >>> f2c(39.0)
      4.0
    """
    return round(((t-32)*5)/9)

def c2f(t):		# THIS FUNCTION CONVERT CELCIUS TO FARENHEIT. BUT I HAD THE SAME PROBLEM I USED THE FLOATING POINT IN THE EXERCISES.
    """
      >>> c2f(0)
      32.0
      >>> c2f(100)
      212.0
      >>> c2f(-40)
      -40.0
      >>> c2f(12)
      54.0
      >>> c2f(18)
      64.0
      >>> c2f(-48)
      -54.0
    """
    return round(((t*9.0)/5) + 32)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
