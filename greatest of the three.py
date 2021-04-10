print ('Enter the 1st number:')
num1=float(input())
print ('Enter the 2nd number:')
num2=float(input())
print ('Enter the 3rd number:')
num3=float(input())

if(num1==num2==num3):
    print("All the 3 numbers are same")
if ((num1>num2)and(num1>num3)):
    print(num1,' is greatest of the 3 given numbers.')
elif ((num2>num3)and(num2>num1)):
    print(num2,' is greatest of the 3 given numbers.')
else:
    print(num3,' is greatest of the 3 given numbers.')


