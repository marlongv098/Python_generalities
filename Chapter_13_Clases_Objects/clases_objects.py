
# WHEN WE CREATE A CLASS ONLY IS NECESSARY TYPE THE CLASS COMAND FOLLOWED BY NAME OF THE CLASS AND A COLON AT THE END.

class point1:		# THIS IS THE NAME OF THE CLASS 
  pass 			# THIS ONE IS A SIMPLE CLASS BY THAT ONLY IS NECESSARY DEFINE WHEREVER WE WANT HERE. THE PASS FUNCTION OR A STRING ETC


# FOR A COMPLEX CLASSES WE CAN DEFINE THE ABOVE CLASS AS FOLLOWS.


class point:				# THIS IS THE CLASS. WHEN THE CLASS DOES NOT HAVE ELEMENT THEN x=0 AND y=0.
   def __init__(self, x=0, y=0):	# DEFINE THE INIT WHERE self REFER TO THE INSTANCE BEING CREATED. IS CUSTOMARY CALLED LIKE THAT.
	self.x = x			# DEFINE THE VARIABLE x
	self.y = y			# DEFINE THE VARIABLE y

   def distance_from_origin(self):			# ANOTHER FUNCTION INSIDE THE CLASS
	return ((self.x**2) + (self.y**2)) ** (0.5) 	# DISTANCE USING self  VARIABLE
	

def print_point(p):				# THE FUNCTIONS BELOW WERE DEFINE OUTSIDE THE CLASS. EACH ONE OF THEM USE THE CLASS TO CALCULATE
    print '%s, %s' % (str(p.x), str(p.y))

def id_point(p):
    print '%s,  %s' % (id(p.x), id(p.y))

def hexa_match(p):
    if int(hex(p.x),16)==p.x and int(hex(p.y),16)==p.y:		# THIS LINE CONVERT AND COMPARE HEXADECIMAL AND DECIMAL NUMBERS.
	print True
    else:
    	print False
	
def show_hexa(p):
    print '%s  %s' % (hex(p.x),hex(p.y))    

p=point(3,4)
print (p.x, p.y)

print p.distance_from_origin()

print_point(p)
id_point(p)
show_hexa(p)
hexa_match(p)

p1=point()
print (p1.x, p1.y)
