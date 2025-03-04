import numpy as np

n = int(input("Enter number of elements : "))
x = []
for i in range(0, n):
    ele = int(input("Enter element: "))
    x.append(ele)
maximum = np.max(x)
minimum = np.min(x)
range = maximum - minimum
print("Max:", maximum)
print("Min:", minimum)
print("Range:", range)
