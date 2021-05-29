

def countdown(n):		# FUNCTION TO COUNTDOWN FROM "n" TO 1 USING "while" FUNCTION
    while n > 0:
        print n			# WITHOUT COMA THE PROGRAM PRINTS A COLUMN.
        n = n-1
    print "Blastoff!"

#countdown(20)

def sequence(n):       # THIS FUNCTION PRINT A SEQUENCE USING "while" FUNCTION WITH THE PARTICULARITIE THAT CONSIDER EVEN AND ODD NUMBERS.TO EACH CASE.
    while n != 1:
        print n,	# THE COMA AFTER "n" PRINT A ROW NUMBER 
        if n % 2 == 0:        # n is even
            n = n / 2
        else:                 # n is odd
            n = n * 3 + 1

#sequence(20)

def num_digits(n):	# THIS IS A COUNTER EXAMPLE. THE COUNTER IS USED TO STORE INFORMATION   
    count = 0
    while n:
        count = count + 1
        n = n / 10
    print count #return count

#num_digits(1055030250)

def num_zero_and_five_digits(n):	# THIS FUNCTION ONLY COUNTS "0" OR "5" DIGITS. NOTHINGELSE.  
    count = 0
    while n:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n / 10
    print count #return count

#num_zero_and_five_digits(12847342340)

#TABLES

def table(k):		# THE MOST IMPORTANT IDEA IN THIS FUNCTION IS THE "\t" FUNCTION IS USED TO TABLE TABULATION. 
	n=1
	while n<k:
		print n, "\t", n*5
		n+=2

#table(14)

def two_dim_tables(n):		# THE IDEA IN THIS FUNCTION IS SHOW THE '  ' SPACE IN THE TABULATION. I HAVE TO SAY ALSO THAT THE COMA AT THE END OF HTE LINE IS SO IMPORTANT BECAUSE ARRAY THE LINES IN DIFERENTS WAYS. IN COLUMS WITHOUT THE COMA AND LINES WITH THE COMA..
	i = 1
	while i <= n:
	    print i, "\t", 2 * i, '\t', i*5, "   ", # PROVED WITH AND WITHOUT COMA.
	    i += 1
	print

#two_dim_tables(10)


#  MULTIPLE DIMENSIONAL TABLES 


def print_multiples(n,k): 	# PRINT MULTIPLES LINES IN A TABLE.
    i = 1
    while i <= k:
        print n * i, '\t',
        i += 1
    print

def table_multiple_tables(n):	# I MUST TAKE CARE HERE BECAUSE THE PROGRAM DEPEND "print_multiples" FUNCTION.
	i = 1
	cat= input("write the numbers of elements in each line of the table ")
	while i <= n:
	    print_multiples(i,cat)
	    i += 1

bet= input("write the numbers of elements in the columns os the table  ")

table_multiple_tables(bet)
