
class point:				# THIS IS THE CLASS. WHEN THE CLASS DOES NOT HAVE ELEMENT THEN x=0 AND y=0.
   def __init__(self, x=0, y=0):	# DEFINE THE INIT WHERE self REFER TO THE INSTANCE BEING CREATED. IS CUSTOMARY CALLED LIKE THAT.
	self.x = x			# DEFINE THE VARIABLE x
	self.y = y			# DEFINE THE VARIABLE y

   def distance_between_points(self,toself):			# ANOTHER FUNCTION INSIDE THE CLASS TO CALCULATE THE DISTANCE. THIS FUNCTION USE self AND ANOTHER ARGUMENT TO CALCULATE THE DISTANCE. TO USE THIS FUNCTION WE HAVE TO PUT IN FRONT OF IT THE FIRST ELEMENT FOLLOWED BY A PERIOD AND THE NAME OF THE FUNCTION INSIDE THE BRAKECTS WE HAVE TO PUT ANOTHER POINT TO CALCULATE THE DISTANCE BETEWEEN THEM
	delta_a = self.x-toself.x				# THIS LINE DEFINE THE x COORDINATE OF THE DIFERENCE
	delta_b = self.y-toself.y				# THIS LINE DEFINE THE y COORDINATE OF THE DIFERENCE
	return (delta_a**2 + delta_b**2)**(0.5)			# THIS LINE RETURN THE DISTANCE.


def distance(q,p):						# THIS FUNCTION WAS DEFINE OUTSIDE THE CLASS BUT USE THE IT TO CALCULATE THE DIFERENCE.
    print ((p.x-q.x)**2 + (p.y-q.y)**2)**(0.5)


p=point(1,2)						# THIS LINE DEFINE THE POINT p USING THE POINT CLASS
q=point(3,4)						# THIS LINE DEFINE THE POINT q USING THE POINT CLASS
distance(p,q)						# THIS LINE CALCULATE THE DISTANCE USING THE OUTSIDE FUNCTION OF THE CLASS

print p.distance_between_points(q)			# THIS LINE CALCULATE THE DISTANCE USING THE CLASS FUNCTION.
