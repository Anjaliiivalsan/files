n=int(input("enter number of numbers"))
list=[]
for i in range(n):
    a = int(input("enter a number"))
    list.append(a)
print(list)
list1=[x**2 for x in list]
print(list1)
