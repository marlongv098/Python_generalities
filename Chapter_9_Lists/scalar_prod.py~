

def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """

    for i in range(len(v)):
      v[i] = s * v[i]	
    return v


def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    #h=0		THIS WAS THE FIRST I DID. THE MAIN DIFERENCE WITH THE NEXT ONE IS I SEPAREATED IN TO FOR AND I THONKING I CAN PUT ALL  TOGETHER. I DID NOT USED THE COUNTER +=1 IN THE FIRST SOLUTION BECAUSE I USED THE "range" OF "len" SUCH AS COUNTER. 
    #for i in range(len(u)):
    #  u[i] *= v[i]
    #for i in range(len(u)):
    #  h += u[i]
    #return h

    s=0			# THIS IS ANOTHER WAY TO DO THE DOT PRODUCT. I FOUND THIS IN YOUTUBE
    l=0
    for i in u:
     s+=i*v[l]
     l+=1
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()

