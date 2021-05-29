expression = raw_input("Enter a boolean expression in two variables, p and q: ") # we must define the logically equivalent boolean expression "p or q" v "p and q".

print " p      q      %s"  % expression  		# print the first line of the table.
length = len( " p      q      %s"  % expression) 	# this line is used to set the numbers of equals in the separator line of the table.
print length*"="					# print an amount of equals 

for p in True, False:
    for q in True, False:
        print "%-7s %-7s %-7s" % (p, q, eval(expression)) #"eval" is a phyton function like "len"
