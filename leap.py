c=int(input("enter current"))
f=int(input("enter final"))
print("future are")
for x in range(c,f+1):
    if(x%4==0 and x%100!=0 or x%400==0):
        print(x)
