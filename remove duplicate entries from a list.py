mlist=[]
noi=int(input("Enter the number of terms :"))
for i in range (1,noi+1):
    print("Enter the term :",i)
    val=input()
    mlist.insert(i,val)
dup=set()
uniq=[]
for x in mlist:
    if x not in dup:
        dup.add(x)
        uniq.append(x)
print("Original list ",mlist)
print("Edited list ",uniq)

    
    
