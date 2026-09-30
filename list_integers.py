x = []
n = int(input("enter any integers: "))
for i in range(n): 
    a = int(input(f"Enter number {i+1}: "))
    if a > 100:
        x.append("over")
    else:
        x.append(a)
print("modified list:", x)