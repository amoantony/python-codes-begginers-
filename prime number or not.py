print('Enter the number:')
num=int(input())
flag=0

for i in range(2,(num)):
     if (num%i)==0:
            flag=1
            break
if flag==1:
        print(num,' is not a prime number ',i,' times ',num//i,' is ',num)
else:
        print(num,'is a prime number')
