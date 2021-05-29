
def is_divisible(num, div): 			# THIS FUNTION WAS MADE TO WORK WITH DIFERENT DIVIDEND AND DIVISOR AND TO KNOW IF THEY ARE DIVISIBLE.. 
	if num % div==0:
		print "Yes, ", num, "is divisible by ", div
	else:
		print "No, ", num, "is not divisible by ", div

cat = input("write the dividend: ")		# I WOULD LIKE KNOW HOW REQUEST BOTH NUMBERS AT THE SAME TIME. 
bet = input("write the divisor: ")
is_divisible(cat, bet)				# THIS A GENERALIZATION OF DIVISIBLE FUNCTION.
