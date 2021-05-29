def only_evens(numbers):
    """
      >>> only_evens([1, 3, 4, 6, 7, 8])
      [4, 6, 8]
      >>> only_evens([2, 4, 6, 8, 10, 11, 0])
      [2, 4, 6, 8, 10, 0]
      >>> only_evens([1, 3, 5, 7, 9, 11])
      []
      >>> only_evens([4, 0, -1, 2, 6, 7, -4])
      [4, 0, 2, 6, -4]
      >>> nums = [1, 2, 3, 4]
      >>> only_evens(nums)
      [2, 4]
      >>> nums
      [1, 2, 3, 4]
    """
    n=[]
    for i in range(len(numbers)):
	if numbers[i] % 2 == 0:
		n+= [numbers[i]]
    return n

def only_odds(numbers):
    """
      >>> only_odds([1, 3, 4, 6, 7, 8])
      [1, 3, 7]
      >>> only_odds([2, 4, 6, 8, 10, 11, 0])
      [11]
      >>> only_odds([1, 3, 5, 7, 9, 11])
      [1, 3, 5, 7, 9, 11]
      >>> only_odds([4, 0, -1, 2, 6, 7, -4])
      [-1, 7]
      >>> nums = [1, 2, 3, 4]
      >>> only_odds(nums)
      [1, 3]
      >>> nums
      [1, 2, 3, 4]
    """
    n=[]
    for i in range(len(numbers)):
	if numbers[i] % 2 != 0:
		n += [numbers[i]]
    return n

def multiples_of(num, numlist):
    """
      >>> multiples_of(3, [1, 3, 4, 6, 7, 8])
      [3, 9, 12, 18, 21, 24]
      >>> multiples_of(1, [2, 4, 6, 8, 10, 11, 0])
      [2, 4, 6, 8, 10, 11, 0]
      >>> multiples_of(2, [1, 3, 5, 7, 9, 11])
      [2, 6, 10, 14, 18, 22]
      >>> multiples_of(4, [4, 0, -1, 2, 6, 7, -4])
      [16, 0, -4, 8, 24, 28, -16]
      >>> nums = [1, 2, 3, 4]
      >>> multiples_of(2, nums)
      [2, 4, 6, 8]
      >>> nums
      [1, 2, 3, 4]
    """
    h=[]
    for i in range(len(numlist)):
	h += [num * numlist[i]]
    return h


if __name__ == '__main__':
    import doctest
    doctest.testmod()
