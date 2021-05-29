
def is_even_number(n):		# THIS FUNCTION IF A NUMBER IS EVEN TELL US "True" AND "False" IF IS ODD. WE CAN ALSO CHANGE THE OPTIONS "False" IF IS EVEN AN "True" IS IF ODD.
	"""
	>>> is_even_number(4)
	True
	>>> is_even_number(3)
	False
	>>> is_even_number(5)
	False
	>>> is_even_number(6)
	True
	"""
	return n % 2==0

if __name__ == '__main__':
    import doctest
    doctest.testmod() 
