import operator
d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
sorted_d = sorted(d.items(), key=operator.itemgetter(1))

print(sorted_d)