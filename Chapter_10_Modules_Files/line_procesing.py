
# WE COULD PUT IN 'oldfile' AND 'newfile' FILES IN ANOTHER FOLDER. ONLU WE HAVE TO PUT THE PATH.


def filter(oldfile, newfile):		# THIS PROGRAM MAKE THE SAME THAT 'copying_files.py'. THE MOST IMPORTANT DIFFERENCE IS THAT THIS FUNCTION TAKE EVERY LINE OF THE FILE AND COPY TO ANOTHER.
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')	# EXAMPLE OF THIS IS 'test2.dat' AND 'test3.dat'.
    while True:
        text = infile.readline()	# WITH THIS LINE WE READ THE FIRST LINE OF THE LOAD FILE.
        if text == "":
           break
        if text[0] == '#':		# THIS LINE READ THE FIRST ELEMENT OF THE FIRST LINE
           continue
        outfile.write(text)
    infile.close()
    outfile.close()
    return


# IN THIS PROGRAM I WAS TRYING TO MAKE A SORTED COPY OF A FILE. IT DOES NOT WORKS WELL YET.

def filter1(oldfile, newfile):		# THIS PROGRAM MAKE THE SAME THAT 'copying_files.py'. THE MOST IMPORTANT DIFFERENCE IS THAT THIS FUNCTION TAKE EVERY LINE OF THE FILE AND COPY TO ANOTHER.
        infile = open(oldfile, 'r')
        outfile = open(newfile, 'w')	# EXAMPLE OF THIS IS 'test2.dat' AND 'test3.dat'.
    #while True:
        text = infile.readlines()
        #if text == "":
        #   break
        #if text[0] == '#':
        #   continue
	outext=['' for x in range(len(text))]
        for i in range(len(text)-1):
	      #for j in range(len(text[i])):
	      if ord(text[i][0]) > ord(text[i+1][0]):
		 outext[i]=text[i+1]
	print outext
#        outfile.write(outext)
#        infile.close()
#        outfile.close()
#        return
