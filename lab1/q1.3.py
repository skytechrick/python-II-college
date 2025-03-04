import random as r
import numpy as np

def calculateMean(list):
    return np.mean(list)

n = int(input("Enter number of elements : "))
x = []

for i in range(0, n):
    ele = r.randint(0, 100)
    x.append(ele)

print("Mean of x: ", calculateMean(x))

