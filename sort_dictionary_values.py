# sort values in dictionary
d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
#sorted_d = sorted(d.items(), key=lambda x: x[1])
sorted_d = sorted((value, key) for (key,value) in d.items())

print(list(d.items()))
print(sorted_d)