# maps apply same function to each element of a sequence
# return modified list
nums = [1,2,3,4,5]

# map(function, list)
print(list(map(lambda x: x**2, nums)))

# same output
def square(num):
    return num**2

print(list(map(square, nums)))