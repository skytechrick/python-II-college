from scipy import stats as sp
import random as r
def mode(x):
    return sp.mode(x)

n = int(input("Enter number of elements : "))
x = []
for i in range(0, n):
    ele = r.randint(0, 100)
    x.append(ele)
print("Mode of x: ", mode(x))
