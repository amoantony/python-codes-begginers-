print('Enter the first term :')
firs=int(input())
print('Enter the last term :')
las=int(input())
for i in range(firs,las):
     for j in range(2,i):
         if (i%j)!=0:
             print(i,end=", ")
             break
         else:
             break

