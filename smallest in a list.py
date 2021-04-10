noi=int(input("Enter the number of terms "))
mlist=[]
for i in range(1,noi+1):
    num=float(input("Enter the term "))
    mlist.insert(i,num)
    if i ==1:
        sml=num
    if sml>num:
        sml=num
print("The smallest of the list is",sml)
