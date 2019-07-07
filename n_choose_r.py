import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

print(nCr(4,2))

f = math.factorial
my_ncr = lambda x,y: f(x) // f(y) // f(x-y)

print("------------------------------------")
print(my_ncr(4,2))