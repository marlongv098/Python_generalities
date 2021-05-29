#print "produces\nthis\noutput"		# FIRST EXERCISE OF THE CHAPTER 6.


def sqrt(n):
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:		# THIS LOOP CONTINUE DOING THE APROXIMATION UNTILL "better==approx" IN THAT CASE THE PROGRAM PRINTS THE OUTPUT 	.
        approx = better
        better = (approx + n/approx)/2.0
    print approx

#sqrt(25)
#sqrt(5)
#sqrt(2)
#sqrt(5.4)

def print_triangular_numbers(n): 	# THIS FUNCTION PRINT TRIANGULAR NUMBERS.  
	i=1
	while i < n+1:
		t=(i*(i+1))/2
		print i,"\t", t
		i+=1

cat = input("wrte the number of triangular number do you want ")

print_triangular_numbers(cat)
