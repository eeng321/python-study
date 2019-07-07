bills = [5,10,20,50,100]

amt = [37,21,109,12,1]
sum = 0
for i in range(len(bills)):
    sum += bills[i] * amt[i]
print(sum)