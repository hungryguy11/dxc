

number1=int(input("Enter the number : "))
i=1
c=0
s=0
while i<=number1:
    if number1%i==0:
        print(i)
        c+=1  
        s+=i
            
    i+=1
print("Count : ", c)
print("Sum : ", s)



