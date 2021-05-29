from line_procesing import *


#filter('unsorted_fruits.txt','sorted_fruits.txt') 	# THIS LINE USE THE line_procesing.py FILE TO MAKE A COPY OF THE "unsorted_fruits.txt" 

def sortfruits(oldfile, newfile):		# THIS FUNCTION SORT THE "oldfile" INTO "newfile"  IS AN EASY WAY TO DO IT.
    infile = open(oldfile, 'r')			# WE OPEN THE FILE TO READ IT 
    outfile = open(newfile, 'w')		# HERE OPEN THE NEW FILE TO WRITE IT. IF THE FILE DOES NOT EXIST THEN IT IS CREATED.
#    text = infile.readlines()
#    text = sorted(text)
#    outfile.writelines(text)
    outfile.writelines(sorted(infile))		# HERE WE SORT THE INFILE WITH THE "sorted" FUNCTION LINE BY LINE WITH THE "outfile.writelines" FUNCTION.
    infile.close()				# HERE WE CLOSE THE 'infile' AND 'outfile'.
    outfile.close()
       

sortfruits('unsorted_fruits.txt','sorted_fruits.txt')
