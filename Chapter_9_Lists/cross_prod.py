


def add_elem_list(j):		# THIS FUNCTION ADD ELEMENTS TO A LIST USING A LOOP. THE RETURN WAS USED TO THE FUNCTION "add_two_list" 
	lis=[]
	count=0
	while count < j:
	  lis.append(input("enter the element: "))
	  count +=1
	#print lis
	return lis

u=add_elem_list(3)		# HERE WE MADE TWO VECTORS.
v=add_elem_list(3)

def cross_product(u,v):
	h=[u[1]*v[2]-v[1]*u[2],	u[0]*v[2]-v[0]*u[2], u[0]*v[1]-v[0]*u[1]]
	print h

def cross_product1(u,v):
	for i in range(len(u)):
	 h[i]=[]

cross_product(u,v)
#for i in range(len(u)):
	  
