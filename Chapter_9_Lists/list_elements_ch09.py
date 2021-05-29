import sys


def add_elem_list(j):		# THIS FUNCTION ADD ELEMENTS TO A LIST USING A LOOP. THE RETURN WAS USED TO THE FUNCTION "add_two_list" 
	lis=[]
	count=0
	while count < j:
	  lis.append(raw_input("enter the element: "))
	  count +=1
	#print lis
	return lis

#cat=input("enter the len of your list: ")
#add_elem_list(cat)


def add_elem_list1(j):		# THIS FUNCTION ADD ELEMENTS TO A LIST USING A FOR LOOP INSIDE A THE LIST
	namelist = [raw_input("Enter a name: ") for i in range(j)]
	#print namelist
	return namelist

#cat=input("enter the len of your list: ")
#add_elem_list1(cat)


def add_two_list(j):		# THIS FUNCTION ADD TWO LIST USING A FUNCTION DEFINED BEFORE. I THINK THIS IS NOT AN EFICIENT FUNCTION BUT DOES IT WORKS. 
	ca=list
	be=list
	ca = add_elem_list(j)
	be = add_elem_list(j)
		
	#print b
	#b = ca.extend(be)
	
	print ca + be

#cat=input("enter the lenth of your lists ")
#add_two_list(cat)


def add_two_list1(j,k):		# THIS IS A BEST PROGRAM TO ADD LISTS. USE THE SAME IDEA OF "add_elem_list1" 
	list1=[raw_input("enter the elements of the first list ") for i in range(j)]
	list2=[raw_input("enter the elements of the second list ") for i in range(k)]
	#print list1 + list2
	

#cat=input("enter the length of each list ")
#add_two_list1(cat)


def good_nested_list(j,k):	# THIS IS A BETTER TWO NESTED LIST FUNCTION. I AM STILL THINKING IS NOT EFICIENT FUNCTION BUT IS USEFULL.I WOULD LIKE DO IN GENERAL..
	list1=[raw_input("enter the elements of the first list ") for i in range(j)]
	list2=[raw_input("enter the elements of the second list ") for i in range(k)]
	print [ list1, list2 ]

#cat=input("enter the length of first list ")
#bet=input("enter the length of second list ")
#add_two_list1(cat,bet)


def double_stuff(k):		# THIS IS A DIFFERENT WAY TO CHANGE A LIST. THIS FUNCTION USE THE "for" LOOP AND "enumerate" PYTHON TOOL SYNTAX. THE ONLY FUNCTION PROBLEM IS DUE THE "raw_input" TOOL.EVERY VALUE IN THE LIST IS AN STRING.       
    a_list=[raw_input("enter the element of the list ") for i in range(k)]
    for index, value in enumerate(a_list):
        a_list[index] = 2 * value
    print a_list

cat=input("enter dimension of the list ")
double_stuff(cat)


def double_stuff1(a_list):	# THIS FUNCTION WORKS WELL USING THE PYTHON SHELL BUT IS NOT NECCESARY THE "print" FUNCTION TO USE IT IN THE SHELL,ALSO THE "raw_input" PROBLEM IS WAS AVOID IN THIS FUNCTION TO IMPORT IT FROM THE SHELL.  . 
	for index, value in enumerate(a_list):
          a_list[index] = 2 * value
	#print a_list




# LATER

def nested_list(j,k): 		# THIS FUNCTION DOES NOT WORK. I WILL COME BACK LATER TO THIS FUNCTION.
	listname=list
	for i in range(j):
	   #for h in range(k):
	   listname=[raw_input("enter the elements: ") for h in range(k)] 	# for h in range(k)]
	print [ listname[i] ]

#cat=input("enter the j coordenate ")	
#bet=input("enter the k coordenate ")
#nested_list(cat,bet)

