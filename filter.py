# filter items out of a sequence
# return filtered list

nums = [1,2,3,4,5]

print(list(filter(lambda x: x % 2 == 0, nums)))
print(list(filter(lambda x: x % 2 != 0, nums)))
print("--------------------------------------------------")

# list comprehension version
print([x for x in nums if x % 2 == 0])
print([x for x in nums if x % 2 != 0])