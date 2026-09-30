print("Simple Calculator")
n1=float(input("Enter first number: "))
op=input("Enter operation:")
n2=float(input("Enter second number: "))
if op=="+":
    res=n1+n2
elif op=="-":
    res=n1-n2
elif op=="*":
    res=n1*n2
elif op=="/":
    if n2!=0:
        res=n1/n2
    else:
        res="Error:Cannot divide by zero"
else:
    res="Invalid operation"
print("Result: ",res)

