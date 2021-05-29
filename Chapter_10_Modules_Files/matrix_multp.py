

def matrix_mult(m1, m2):
    """
      >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
#    m1Row=len(m1)
#    m1Col=len(m1[0])
#    m2Row=len(m2)
#    m2Col=len(m2[0])
#    h=[[0 for x in range(m2Col)] for y in range(m1Row)]
#	    if m1Col==m2Row:			
#	    for i in range(m1Row):		# THIS CHUNK OF CODE CACULATE THE MATRICES MULTIPLY. IS USEFULL BECAUSE DO ALL THE PRODUCT IN THREE LINES
#		for j in range(m2Col):
#		   for k in range(m1Col):
#			h[i][j] += m1[i][k] * m2[k][j]
#	    return h
#    else: 
#	    return "The matrices can not be multiplied"


    d=[]	# IN THIS CODE I DID NOT NEED IT AN INITIAL MATRIX OF ZEROS TO STORE THE FINAL MATRIX "d". ONLY WAS NECCESARY A VECTOR TO STORE THE RESULT. THAT IS THE REASON THE "append" FUNCTION IS USEFULL.. 
    i=0
    while i<len(m1):
      j=0
      e=[]	
      while j<len(m2[0]):
	 k=0
	 r=0
	 while k<len(m2):	 # HERE I MUST DO A REMARK. THIS CODE ALSO WORKS WITH A m1[0]. THAT HAPPEN BECAUSE IN A MATRIX MULTIPLICATION  THE    "len(m1[0])=len(m2)"
	   r += m1[i][k] * m2[k][j]
	   k+=1
	 j+=1
	 e.append(r)
      d.append(e)
      i+=1
    return d


if __name__ == '__main__':
    import doctest
    doctest.testmod()

