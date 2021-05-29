


def scalar_mult(s, m):		# I USED THE SAME "add_matrices.py" SYNTAX AND WORKS WELL.
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    h=[[0 for x in range(len(m[0]))] for y in range(len(m))] 	# THIS THE THE MEMORY SPACE TO STORE THE SUM MATRIX. I LIKE THIS FORM TO STORE THE ZERO MATRIX . 
    for i in range(len(m)):
      for j in range(len(m[0])):
         h[i][j] = m[i][j] * s		# NOW WE CALCULATE THE THE MATRICES SCALAR PRODUCT..
    return h


if __name__ == '__main__':
    import doctest
    doctest.testmod() 
