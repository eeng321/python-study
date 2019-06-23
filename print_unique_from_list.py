import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
output = []
for i in range(n):
    s = input()
    string = []
    for i in s:
        if i not in string:
            string.append(i)
    output.append(''.join(string))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in output:
    print(i)