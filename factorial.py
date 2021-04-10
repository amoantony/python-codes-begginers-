print('enter the number ')
num=int(input())
na=1
if num<0:
    print('No factorial for -ve numbers')
elif num==0:
    print('factorial is 1')
elif num>=1:
    for i in range(1,num+1):
        na=na*i
print('Factorial of ',num,' is ',na)
    
        
