import re
import statistics

number = input("Give random numbers separated with random characters: ")
xList = re.findall(r'[-+]?[\d]+', number)

for i in range(len(xList)): 
    xList[i] = int(xList[i]) 

print("SUM:")
print(round(sum(xList), 1))
print("MEDIAN:")
print(round(statistics.median(xList), 1))
print("MEAN:")
print(round(statistics.mean(xList), 1))
