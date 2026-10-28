list1=[1,2,4,3,8]
list2=[1,2,4,3,5]
print("the first list is:"+str(list1))
print("the second list is:"+str(list2))
sum1=0
sum2=0
for x in range(0,len(list1)):
    sum1=sum1+list1[x]
print("the sum of all elements in given list1:",sum1)
for x in range(0,len(list2)):
    sum2=sum2+list2[x]
print("the sum of all elements in given list2:",sum2)
if sum1==sum2:
    print("list sum to same value")
else:
    print("list are of different sum")