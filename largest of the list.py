noi=int(input("Enter the number of terms :"))
mlist=[]
for i in range(1,noi+1):
    val=int(input("Enter the number "))
    mlist.insert(i,val)
    if i==1:
        grt=val
    if grt<val:
        grt=val
print("The largest number is ",grt)
