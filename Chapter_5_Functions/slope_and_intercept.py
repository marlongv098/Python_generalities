
def slope(x1, y1, x2, y2):	# THIS FUNCTION CALCULATES THE SLOPE OF THE LINE.
    """
      >>> slope(5.0, 3.0, 4.0, 2.0)
      1.0
      >>> slope(1.0, 2.0, 3.0, 2.0)
      0.0
      >>> slope(1.0, 2.0, 3.0, 3.0)
      0.5
      >>> slope(2.0, 4.0, 1.0, 2.0)
      2.0
    """
    return (y2-y1)/(x2-x1)

def intercept(x1, y1, x2, y2):		# THIS FUNCTION CALCULATES THE "y" INTERCEPTION OF THE LINE EQUATION USING THE SLOPE FUNCTION.
    """
      >>> intercept(1.0, 6.0, 3.0, 12.0)
      3.0
      >>> intercept(6.0, 1.0, 1.0, 6.0)
      7.0
      >>> intercept(4.0, 6.0, 12.0, 8.0)
      5.0
    """
    return (-slope(x1,y1,x2,y2) * x1 ) + y1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

