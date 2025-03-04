import statistics as st
import random as r
n = int(input("Enter the number of elements: "))
x = []
for i in range(n):
    x.append(r.randint(1, 100))
print("Variance:", st.variance(x))