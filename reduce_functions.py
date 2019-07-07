# applies same operation to items of a sequence
# uses result of operation as first param of next operation
# returns an item, not a list
from functools import reduce

nums = [1,2,3,4]
print(reduce(lambda x,y: x*y, nums))
print("-------------------------------------------")
# sum function using reduce
l = list(range(1, 10))
print(l)
print(reduce(lambda x,y: x+y, l))
