

def add_matrices(m1,m2):  	# THIS IS THE SUM MATRICES FUNCTION
    """
      >>> a = [[1, 2], [3, 4]]
      >>> b = [[2, 2], [2, 2]]
      >>> add_matrices(a, b)
      [[3, 4], [5, 6]]
      >>> c = [[8, 2], [3, 4], [5, 7]]
      >>> d = [[3, 2], [9, 2], [10, 12]]
      >>> add_matrices(c, d)
      [[11, 4], [12, 6], [15, 19]]
      >>> c
      [[8, 2], [3, 4], [5, 7]]
      >>> d
      [[3, 2], [9, 2], [10, 12]]
    """
    m1Row=len(m1)	# ONLY WAS NECESSARY ONE OF THE MATRIX DIMENSION THAT WAS THERE DUE TO THE MATRICES SUM SHOULD HAVE THE SAME DIMENSION..
    m1Col=len(m1[0]) 	
    m2Row=len(m2)
    m2Col=len(m2[0])
    h=[[0 for x in range(m1Col)] for y in range(m1Row)]   # THIS THE THE MEMORY SPACE TO STORE THE SUM MATRIX. I LIKE THIS FORM TO STORE THE ZERO MATRIX . 
    for i in range(m1Row):		# NOW WE CALCULATE THE THE MATRICES SUM.
      for j in range(m1Col):
        h[i][j]= m1[i][j] + m2[i][j] #for j in range(m1Col)]
    #for i in range(0,len(h),2):
    #  h[i]+=h[i] 
    return h

    #matrixSum = m[i] + n[i] for i in range 
    #return matrixSum 
   
if __name__ == '__main__':
    import doctest
    doctest.testmod()
