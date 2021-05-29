
def function_a():			# define the called functions
    print "function_a was called..."

def function_b():
    print "function_b was called..."

def function_c():
    print "function_c was called..."


def dispatch(choice):			# this is the election function
	if choice == 'a':
	    function_a()
	elif choice == 'b':
	    function_b()
	elif choice == 'c':
	    function_c()
	else:
	    print "Invalid choice."

cat = raw_input("make your choice a, b or c: ")		# request an string input election "raw_input"

dispatch(cat)						# print the election function.

