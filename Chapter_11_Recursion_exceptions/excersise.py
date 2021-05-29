

def swap(x, y):      # incorrect version
     print  "before swap statement: id(x):", id(x), "id(y):", id(y)
     x, y = y, x
     print  "after swap statement: id(x):", id(x), "id(y):", id(y)

a, b = 0, 1
print  "before swap function call: id(a):", id(a), "id(b):", id(b)
swap(a, b)
print  "after swap function call: id(a):", id(a), "id(b):", id(b)



# THE EXERCISE 8 IS REPRESENTED IN THE LINES ABOVE

nums = [1, 2, 3, 4]

[x**3 for x in nums]

[x**2 for x in nums if x**2 != 4]

[(x, y) for x in nums for y in nums]

[(x, y) for x in nums for y in nums if x != y]


