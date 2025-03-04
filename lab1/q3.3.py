import numpy as np
import random as r

n = int(input("Enter number of elements : "))
x = []
for i in range(0, n):
    ele = r.randint(0, 100)
    x.append(ele)
median = np.median(x)
print("Median : ", median)