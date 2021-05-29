import os
#from os import * this does not works

def new_line(): #this define a empty space function
	print 

def many_lines():
	for i in range(20):
		print


def finish():
	#os.system("clear")  		#both solutions works well
	absolutely_unused_variable = os.system("clear")       # are made to shell prompt clear

def empty_lines():
	many_lines() #this line print all empty space once
	#new_line() #these lines print one by one empty space
	#new_line()
	#new_line()
	#new_line()
	#new_line()
	#new_line()
	#finish()    #this line clear the shell prompt
	print 1

empty_lines()

#print empFirst line"  #those was proves to show what i was doing.
#print "Second line"
	
#print "Third line"
