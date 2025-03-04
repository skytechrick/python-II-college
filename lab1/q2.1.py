from scipy import stats as sp

def mode(x):
    return sp.mode(x)

x = [5, 6, 7, 7, 8, 9]
print("Mode of x: ", mode(x))
