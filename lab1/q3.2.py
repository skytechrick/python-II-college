import numpy as np

n = int(input("Enter number of elements : "))
x = []
for i in range(0, n):
    ele = int(input("Enter element: "))
    x.append(ele)
median = np.median(x)
print("Median : ", median)