#!/usr/bin/env python

import os
import sys

# THIS FUNCTION SHOW US THE FILES AND DIRECTORIES INSIDE A FOLDER. WHEN YOU EXECUTE THE PROGRAM IF ONLY HAVE AN ARGUMENT THE FUNCTION TREE PRINT ON THE SCREEN THE FILES AND DIRECTORIES INSIDE THE FOLDER YOU ARE AXECUTING. BUT INSTEAD IF IN THE EXECUTION YOU PUT A VALID PATH IN YOUR SYSTEM THE PROGRAM PRINT OUT THE FOLDERS AND DIRECTORIES IN THAT PATH..



# FUNCTION TO EVALUATE THE GIVEN PATH IN THE EXECUTION PROGRAM. AN DEFINE THE tree_root VARIABLE 

def getroot():				
    if len(sys.argv) == 1:		# IF THE SECOND ARGUMENT IS EMPTY THIS LINE IS USED.
        path = ''
    else:				# IF THE SECOND ARGUMENT IS NOT EMPTY THIS LINE IS USED.
        path = sys.argv[1]		# sys.argv[1] IS THE SECOND ARGUMENT SHOWED TO THE PROGRAM IN THE SHELL.

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
    return dirlist						# THIS ONE PRINT THE SORTED LIST.



# THIS FUNCTION PRINTS OUT THE PREFIX, FILES AND DIRECTORIES IN THE GIVEN PATH.



def traverse(path, prefix='|--', s='.\n', f=0, d=0):

    dirlist = getdirlist(path)				# USE THE getdirlist TO CREATE AND SORT A LIST WITH ELEMENTS IN path FOLDER.

    for num, file in enumerate(dirlist):		# ENUMERATE THE ELEMENTS OF THE dirlist (FILE VARIABLE AND NUM ARE THE INDEX)  
        lastprefix = prefix[:-3] + '`--'		# THIS LINE CHANGE THE PREFIX DEFINED IN THE ARGUMENTS FUCNTION |-- TO `--
        dirsize = len(dirlist)				# LEN OF THE dirlist

        if num < dirsize - 1:				# 
            s += '%s %s\n' % (prefix, file)		# THIS LINE PRINT THE PREFIX AND THE FILE.
        else:
            s += '%s %s\n' % (lastprefix, file)		# THIS LINE DO THE SAME THAT THE LINE ABOVE BUT THIS CHANGE THE LAST LINE PREFIX..

        path2file = os.path.join(path, file)		# THIS LINE JOIN THE GIVEN PATH TO EVERY ELEMENT IN THE FOLDER. i.e. path2file = path/file/ 

        if os.path.isdir(path2file):			# IF THE ELEMENT path2file IS A DIR THEN THIS CHUNK OF CODE IS USED.
            d += 1					# THIS LINE COUNT AND STORE THE AMOUNT OF DIRECTORIES IN A FOLDER
            if getdirlist(path2file):			# USE THE getdirlist TO CREATE AND SORT A LIST WITH ELEMENTS IN path2file FOLDER.
                s, f, d = traverse(path2file, '|   ' + prefix, s, f, d)		# HERE THEY USE RECURSION TO START AGAIN THE PROCESS WITH THE NEW FOLDER. THE VARAIBLES path AND PREFIX CHANGE AND THE s, f, d, STILL COUNTIG ELEMENTS IN THE FOLDER.
        else:
            f += 1 					# f STORE AND COUNT THE AMOUNT FILES IN A FOLDER

    return s, f, d					# THIS LINE RETURN THE PREFIX (STRINGS) - FILES - DIRECTORIES.


if __name__ == '__main__':
    root = getroot()					# THIS LINE CREATES THE tree_root PATH.USING THE PATH
    tree_str, files, dirs = traverse(root)		# THIS LINE USE traverse FUNCTION TO STORE THE ELEMENTS WHICH ARE GOING TO BE PRINTED.

#    print root

    if dirs == 1:					# THESE LINES ARE USED TO PRINT THE AMOUNT OF ELEMENTS ON THE SCREEN AFTER 
        dirstring = 'directory'
    else:
        dirstring = 'directories'
    if files == 1:
        filestring = 'file'
    else:
        filestring = 'files'

    print tree_str							# THIS LINE PRINT THE ELEMENTS INSIDE EVERY FOLDER IN THE PATH ON THE SCREEN.
    print '%d %s, %d %s' % (dirs, dirstring, files, filestring) 		# THIS IS THE LAST LINE PRINTED.


