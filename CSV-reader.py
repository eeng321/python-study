import csv

f = open(r"C:\Users\eeng\Documents\python-study\menu.csv")
r = csv.reader(f)
data = list(r)

for i in range(len(data)):
    if "Won" in data[i][1]:
        print(data[i])