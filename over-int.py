x = []
n = int(input("Enter the number of integers: "))

for i in range(n):
    a = int(input(f"Enter integer {i+1}: "))
    if a > 100:
        x.append('over')
    else:
        x.append(a)

print("modified list:", x)