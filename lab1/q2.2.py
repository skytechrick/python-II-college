from scipy import stats as sp

def mode(x):
    return sp.mode(x)

n = int(input("Enter number of elements : "))
x = []
for i in range(0, n):
    ele = int(input("Enter element: "))
    x.append(ele)
print("Mode of x: ", mode(x))
