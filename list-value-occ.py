list1=[1,2,4,3,8]
list2=[1,2,4,3,5]
print("the first list is:"+str(list1))
print("the second list is:"+str(list2))
print("the value occur in both list:")
for x in list1:
    if x in list1 and x in list2:
        print(x)