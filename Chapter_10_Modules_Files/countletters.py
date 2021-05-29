#
# countletters.py
#

from sys import argv

#argv[1]



def display(i):			# THE "display" FUNCTION SHOW THE PYTHON LETTER VALUE. 
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE'
    return chr(i)			# FUNCTION THE "chr(int)" RETURN THE LETTER RELATED TO THAT NUMBER.

infile = open('alice_in_wonderland.txt', 'r')		# THIS CHUNK OF PROGRAM OPEN AND READ THE FILE 
text = infile.read()
infile.close()

counts = 128 * [0]			# MAKE A ZERO LIST TO STORE THE COUNTED LETTERS. EACH ENTRY OF THE LIST IT IS GOING TO STORE THE AMOUNT OF SAME LETTERS IN THE TEXT. SOME OF THE ENTRIES WILL BE EMPTY. 

for letter in text:
    counts[ord(letter)] += 1			# THE FUNCTION "ord('letter')" RETURN THE INTEGER VALUE OF THE LETTER AND "counts" STORE AND COUNT THE AMOUNT OF SAME LETTERS IN THE TEXT.

outfile = open('alice_counts.dat', 'w')			# THIS CHUNK PRINT THE HEAD OF THE OUTFILE "alice_counts.dat"
outfile.write("%-12s%s\n" % ("Character", "Count"))
outfile.write("=================\n")

for i in range(len(counts)):			# THIS ONE USE THE "display" FUNCTION TO KNOW THE TEXT LETTER AND "counts" FUNCTION TO PRINT THE AMOUNT OF SAME LETTER IN THE "alice_counts.dat"  FILE.  
    if counts[i]:				# THIS ONE CONSIDER ONLY THE coutns ENTRIES WHICH HAVE ELEMENTS AND DISMISS THE EMPTY ENTRIES.
        outfile.write("%-12s%d\n" % (display(i), counts[i]))	# TO PRINT THE OUTFILE THEY USE A -12 SPACE IN BOTH CHUNKS THE HEAD AND THIS ONE. 

outfile.close()
