

import os 
import sys


# FUNCTION TO EVALUATE THE GIVEN PATH IN THE EXECUTION PROGRAM. AN DEFINE THE tree_root VARIABLE 


def getroot():				
    if len(sys.argv) == 1:		# IF THE SECOND ARGUMENT IS EMPTY THIS LINE IS USED.
        path = ''
    else:				# IF THE SECOND ARGUMENT IS NOT EMPTY THIS LINE IS USED.
        path = sys.argv[1]		# sys.argv[1] IS THE SECOND ARGUMENT SHOWED TO THE PROGRAM IN THE SHELL.
    	tree_root=path
    if os.path.isabs(path):		# IF THE PATH IS ABSOLUTE (/home/trabajo/etc) THEN THIS LINE IS USED. 
        tree_root = path		
    else:
        tree_root = os.path.join(os.getcwd(), path)		# THIS IS USED WHEN THE SECOND ARGUMENT IS EMPTY i.e THIS IS USED WHEN path=''. THE os.path.join() JOIN CURRENT WORKING DIRECTORY TO THE PATH VARIABLE. THE os.getcwd() RETURN A STRING OF THE CURRENT WORKING DIRECTORY.

    return tree_root


# ONCE THE PATH WAS DEFINED THIS FUNCTION TAKES THE PATH AND MAKE A LIST WITH THE ELEMENTS INSIDE THE FOLDER


def getdirlist(path):				
    dirlist = os.listdir(path)					# os.listdir() PUT THE ELEMENTS (DIRECTORIES AND FOLDERS) INSIDE A FOLDER.IN A LIST.
    dirlist = [name for name in dirlist if name[0] != '.']	# THIS LINE ERASE THE FIRST LINES OF THE LIST WHICH START WITH A POINT i.e. "." AND ".."
    dirlist.sort()						# THIS ONE SORT THE LAST LIST. 
    return dirlist


# THIS FUNCTION REMOVES THE FILES INSIDE EACH FOLDER IN THE PATH.


def removefile(path):
	os.chdir(path)
	dirlist=getdirlist(path)
	for num, file in enumerate(dirlist):		# THIS LINE IS USED TO GO TO A FOLDER PATH. THE EQUIVALENCY OF CD IN THE SHELL PROMPT.
		if file=='trash.txt':	
		    os.remove(file)
	#return


def traverse(path):
    dirlist=getdirlist(path)				# SORT AND MAKE A LIST OF THE ELEMETS IN THE PATH.
    if len(sys.argv)==1:				# EXECUTE WHEN THE PATH ARGUMENT DOES NOT EXIST
	removefile(path)					# CREATES THE FILE ONLY INSIDE THE FOLDER WHERE WE ARE EXECUTING

    else:						# EXECUTE WHEN THE PATH ARGUMENT EXIST
	removefile(path)	    					# MAKE THE FILE trash.txt IN THE FOLDER GIVEN LIKE ARGUMENT
	for num, file in enumerate(dirlist):		# 
	    path2=os.path.join(path,file)		# MAKE NEW PATHS
	    if os.path.isdir(path2):			# EVALUATE IF THE ELEMETS INSIDE THE MAIN FOLDER.ARE DIRECTORIES
				
		newfile=removefile(path2)			# MAKE NEW FILES trash.txt INSIDE EVERY SUB-FOLDER OF THE MAIN FOLDER
		if getdirlist(path2):			# SORT AND MAKE A LIST OF THE DIRECTORIES INSIDE EACH SUB-FOLDER
		    traverse(path2)			# USE RECURSION TO MAKE A trash.txt FILE IN EVERY SUB-FOLDER OF A SUB-FOLDER......



if __name__ == '__main__':

	root=getroot()			# DEFINED THE PATH.
	traverse(root)			# PUT THE PATH IN TRAVERSE TO MOVE INTO THE FOLDERS.

