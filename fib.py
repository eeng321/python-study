from functools import reduce

print("Iterative For-Loop")
a = 0
b = 1
for i in range(10):
    print(a)
    a, b = b, a + b

# one liner fib function
fib = lambda n: reduce(lambda x,n: [x[1], x[0]+x[1]], range(n), [0,1])[0]
print("---------------------------------")
print("Lambda")
print(list(map(fib, range(10))))
print("---------------------------------")

# fib function generator
def fibs():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b, a + b

print("Generator")
my_fib = fibs()
for i in range(10):
    print(next(my_fib))

print("---------------------------------")
print("Recursion")

def refib(n):
	if n <= 1:
		return n
	else:
		return refib(n-1) + refib(n-2)

for i in range(10):
	print(refib(i))