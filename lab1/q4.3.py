import numpy as np
import random as r

n = int(input("Enter number of elements : "))
x = []
for i in range(0, n):
    ele = r.randint(0, 100)
    x.append(ele)
maximum = np.max(x)
minimum = np.min(x)
range = maximum - minimum
print("Max:", maximum)
print("Min:", minimum)
print("Range:", range)
