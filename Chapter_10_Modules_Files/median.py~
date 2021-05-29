
from sys import argv
import string
import numpy

nums = argv[1:]

for index, value in enumerate(nums):
    nums[index] = float(value)

nums.sort()		  					# THIS CODE SORT THE ARGUMENTS
if len(nums)%2==0:						# THIS LINE EVALUATE THE LEN OF THE ARGUMENTS. IN THIS CASE IF IS EVEN DO.. 
  print (nums[(len(nums)/2)-1]+ nums[len(nums)/2])/2		#  HERE WE ARE DOIGN AN AVERAGE OF THE ELEMENTS TO FIND THE MEDIAN. THAT AVERAGE IS THE MEAN OF THE ELEMENTS IN THE CENTRE OF THE LIST..
else:
  print nums[len(nums)/2] 					# FOR THE ODD CASE WE ONLY TAKE THE ELEMENT ON THE MIDDLE

