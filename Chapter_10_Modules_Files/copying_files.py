

def copy_file(oldfile, newfile):	# WHEN I IMPORT THE MODULE AS "import module" THE FUNCTION GAVE ME AN ERROR. THE ERROR SAID  "'copy_file' is not defined". BUT WHEN I IMPORT THE MODULE AS "from module imort *" I DID NOT HAD THAT PROBLEM AND THE FUNCTIONS WORKED WELL. I HOPE KNOW WHAT IS THE CAUSE OF THIS PROBLEM IN A FUTURE  
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')		# THIS FUNCTION TAKE A FILE AND MAKE ANOTHER WITH THE SAME INFORMATION INSIDE THE FIRST ONE.
    while True:
        text = infile.read(50)			# EXAMPLES OF THIS IS "test.dat" AND "test1.dat"
        if text == "":
            break
        outfile.write(text)
    infile.close()
    outfile.close()
    return  
