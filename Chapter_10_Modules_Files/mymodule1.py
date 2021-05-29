
myage=34
year=2015

print "My name is %s" % __name__ 	# THIS LINE GAVE THE NAME OF THE FILE IS GOING TO PRINT THE MODULE NAME IF THE FILE IS IMPORTED AND IT IS GOING TO PRINT main IF IS THE EXECUTED MAIN FILE.

if __name__ == '__main__':		# THIS IS USED TO PRINT THE IMFORMATION ONLY IF THE NAME OF THE FILE IS "main" 
    print "This won't run if I'm  imported."

