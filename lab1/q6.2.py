import statistics as st

n = int(input("Enter the number of elements: "))
x = []
for i in range(n):
    x.append(int(input("Enter element: ")))
print("Standard deviation of x:", st.stdev(x))