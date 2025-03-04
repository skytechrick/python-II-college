import statistics as st

n = int(input("Enter the number of elements: "))
x = []
for i in range(n):
    x.append(int(input("Enter the element: ")))
print("Variance:", st.variance(x))