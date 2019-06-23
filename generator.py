## generators do not need to put all values into memory at once.
## generators yield 1 value at a time, list puts all values into memory

# #method 1, regular 
# def square_numbers(nums):
#     for i in nums:
#         yield (i * i)
# my_nums = square_numbers([1,2,3,4,5])

# #method 2, list comprehension gives a list
# my_nums = [x*x for x in [1,2,3,4,5]]

#method 3, list comprehension using generator
my_nums = (x*x for x in [1,2,3,4,5])

print(my_nums)
for num in my_nums:
    print(num)