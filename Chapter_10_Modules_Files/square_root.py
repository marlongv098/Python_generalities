
def print_square_root(x):		# IN THIS EXERCISE WE CALCULATE THE SQUARE ROOT OF A NUMBER USING LOOPS. BUT WE COULD FIND THE SAME RESULT USING "math.sqrt" FUNCTION OF THE "math" MODULE.  
    if x <= 0:
        print "Positive numbers only, please."
        return

    result = x**0.5
    print "The square root of", x, "is", result

num=input("ingrese cantidad: ")
print "your number was ", num

print_square_root(num)
