# PURE FUNCTIONS AND MODIFIERS


def add_elem_list(j):		# THIS FUNCTION ADD ELEMENTS TO A LIST USING A LOOP. THE RETURN WAS USED TO THE FUNCTION "add_two_list" 
	lis=[]
	count=0
	while count < j:
	  lis.append(raw_input("enter the element: "))
	  count +=1
	#print lis
	return lis		# THE "return" IS BETTER TO THIS PURPOSE. USING EMBEDDED FUNCTIONS. 


#add_elem_list(cat)


def double_stuff1(a_list):	# THIS FUNCTION WORKS WELL USING THE PYTHON SHELL BUT IS NOT NECCESARY THE "print" FUNCTION TO USE IT IN THE SHELL. . 
	for index, value in enumerate(a_list):
          a_list[index] = 2 * value
	return a_list


#cat=input("enter the len of your list: ") 	# I WAS USING TWO FUNCTIONS OF "list_elements_ch09.py" TO MAKE A LIST, IT WORKS WELL BUT IT STILL HAVING THE SAME PROBLEM. THE FUNCTION ONLY RECOGNIZE STRING DUE THE "raw_input" FUNCTION.

#double_stuff1(add_elem_list(cat))


def double_stuff2(a_list):		 # THIS FUNCTION TAKE A LIST A MAKE ANOTHER LIST. THE DIFFERENCE WITH THE ABOVE FUNCTIONS IS THIS ONE DO NOT CHANGE THE FIRST LIST. THIS FUNCTION STORE THE NEW LIST IN A CHUNK OF MEMORY COMPLETELY DIFFERENT.TO THE FIRST ONE.
    new_list = []
    for value in a_list:
        new_list += [2 * value]
    return new_list





