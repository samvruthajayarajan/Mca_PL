x=int(input("Enter any number to be reversed: "))
rev=0
while x>0:
    rev=(rev*10)+(x%10)
    x=x//10
    print("The reversed number is ",rev)