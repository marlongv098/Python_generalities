

def add_row(matrix):  		# ONE PARTICULARITY ABOUT THE DOCTEST FUNCTION IS RELATED TO THE NEXT PARAGRAPH. WE CAN PUT MESSAGES TO THE PEOPLE WHO IS GOING TO USE THE MODULE WE ARE MAKING. WE COULD SEE AN EXAMPLE OF THIS IN THE NEXT LINE INSIDE THE DOCTEST.   
    """
      this function add the zero vector to the row. on ly es necessary define the matrix.
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    matrixRows=len(matrix)
    matrixColums=len(matrix[0])
    #for i in range(matrixRows):    
    #matrix = matrix.append([matrixRows * [0]])
    #return matrix
    #for x in range(len(matrix)):
    #for i in range(len(matrix)):
	#matrix = matrix*[0]
    #return matrix
    matrix = matrix + [[0 * matrixRows for i in range(matrixColums)]]
    return matrix

def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    matrix = [x + [0] for x in matrix]
    return matrix

    #for x in matrix:
	#matrix=[x+[0]]
    #return matrix



def row_times_column(m1, row, m2, column):
    """
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)	#[1,2]*[5,7]
      19
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)	#[1,2]*[6,8]
      22
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
      43
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
      50
    """
    
    a=m1[row]		#  THIS CHUNK OF CODE FIND THE MATRIX ELEMENTS TO MULTIPLY. AFTER THAT ONLY IS NECESSARY MAKE THE "dot_produt".
    b=[]
    for i in range(len(m2[0])):
      b+=[m2[i][column]]		# 
    #return [a,b]

    h=0				# THIS CHUNK CALCULATE THE "dot_produt" OF TWO VECTORS
    #for i in range(len(a)):
    #  a[i] *= b[i]
    #for i in range(len(a)):
    #  h += a[i]
    for i in range(len(a)):	# THIS CHUNK CALCULATE THE "dot_produt" OF TWO VECTORS
	a[i]*=b[i]
	h+=a[i]
    return h	

    
    

def matrix_mult(m1, m2):
    """
      >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    m1Row=len(m1)
    m1Col=len(m1[0])
    m2Row=len(m2)
    m2Col=len(m2[0])
    h=[[0 for x in range(m2Col)] for y in range(m1Row)]
    if m1Col==m2Row:			
	    for i in range(m1Row):		# THIS CHUNK OF CODE CACULATE THE MATRICES MULTIPLY. IS USEFULL BECAUSE DO ALL THE PRODUCT IN THREE LINES
		for j in range(m2Col):
		   for k in range(m1Col):
			h[i][j] += m1[i][k] * m2[k][j]
	    return h
    else: 
	    return "The matrices can not be multiplied"

    #if m1Col==m2Row:		# I WAS TRYING CODE THE 
	 #a=[]
	 #b=[]
	 #for i in range(m1Row):
    	    #a+=m[i]     		#  THIS CHUNK OF CODE FIND THE MATRIX ELEMENTS TO MULTIPLY. AFTER THAT ONLY IS NECESSARY MAKE THE "dot_produt".
    	 #b=[]
	 #for i in range(m2Row):		# OR "m1Col" IS THE SAME 
	 #     a += [m1[i]]		# 
	 #     for j in range(m2Col):
	 #	    b += [m2[i][j]]
	            
         #return [a,b]
	 #return b
	


if __name__ == '__main__':
    import doctest
    doctest.testmod()
