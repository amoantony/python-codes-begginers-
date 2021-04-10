print('enter the number ')
num=int(input())

def facto(i):
    if i==1:
       return i
    else:
        return i*facto(i-1)
i=facto(num)
print(i)
    
        
