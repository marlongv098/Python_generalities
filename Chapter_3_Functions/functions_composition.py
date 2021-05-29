phi=3.1416

def area_cir(rad):			# FUNCTION CIRCUNFERENCE AREA.
	return phi*(rad**2)

def distance(x1,x2,y1,y2):		# FUNCTION DISTANCE BETWEEN TWO POINTS.
	dx=x1-x2
	dy=y1-y2
	suma=(dx**2)+(dy**2) 	 
	square=suma**0.5
	return square
	#print square

cat= input("write x center of circunference ")
bet= input("write y center of circunference ")
cet= input("write x perimeter of circunference ")
dot= input("write y perimeter of circunference ")


def area2(x,y,z,w):				# FUNCTION TO THE COMPOSITION OF FUNCTIONS AREA AND CIRCUNFERENCE.
	return area_cir(distance(x,y,z,w))

area2(x,y,z,w)
#distance(3,4,5,6)


