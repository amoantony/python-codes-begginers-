mlist=[]
print("Number of elements ")
noe=int(input())
for i in range(1,noe+1):
    print("Enter the term no: ",i)
    num=float(input())
    mlist.insert(i,num)

nlist=mlist
prod=1
for i in range(0,noe):
    popp=mlist.pop()
    prod=prod*popp
   
print("The product of the given numbers is ",prod)
    
