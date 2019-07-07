s = "hello cute doggo"
print(s)
print(s[::-1])

arr = s.split()
print(arr)
rs = ""
# iterate backwards (start, stop, step)
for i in range(len(arr)-1, -1, -1):
    rs += arr[i] + " " 
print(rs.strip()) # get rid of last space

# iterate after reversing the split string
rev = ""
for i in arr[::-1]:
    rev += i + " "
print(rev.strip()) # get rid of last space