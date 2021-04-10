#def sumof(items):
#    summ=0
#    for i in range(1,noe+1):
#        summ=summ+items[i]
#    print(summ)
    

mlist=[]
print("Number of elements ")
noe=int(input())
for i in range(1,noe+1):
    print("Enter the term no: ",i)
    num=float(input())
    mlist.insert(i,num)
print(sum(mlist))
#sumof(mlist)


            
