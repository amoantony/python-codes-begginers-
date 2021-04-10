num=int(input("Enter the number upto :",))
print("Fibonacci series up to ",num," is ")
i=0
j=1
for t in range(0,num+1):
    print(i,end=", ")
    f=i
    i=j
    j=i+f
