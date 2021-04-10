count=0
noi=int(input("No of terms :"))
for i in range (0,noi):
    mstr=input("Enter the string :")
    if len(mstr)>2 and mstr[1]==mstr[-1]:
        count=count+1
print("No of strings with length more than 2 and first and last character same are :",count)
