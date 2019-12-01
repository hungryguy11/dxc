#pattern 1
print("-----PATTERN 1-----")
a=int(input("enter no."))
for i in range(a+1):
	print("*"*i)

#pattern 2
print("-----PATTERN 2-----")
a=int(input("enter no."))
for i in range(a,0,-1):
	print("*"*i)

#pattern 3
print("-----PATTERN 5-----")
a=int(input("enter no."))
s=0
for i in range(a,0,-1):
	s=a-i
	print(" "*s+"*"*i)

#pattern 4
print("-----PATTERN 4-----")
a=int(input("enter no."))
for i in range(a+1):
	s=a-i
	print(" "*s+"*"*i)



#pattern 5
print("-----PATTERN 5-----")
a=int(input("enter no."))
for i in range(a+1):
	s=a-i
	print(" "*s+"* "*i)



#pattern 6
print("-----PATTERN 6-----")
string = input("Enter String: ")
lines=len(string)

i=1
spaces=(lines-1)
letter=1

while i<=lines:
    print(" "*(spaces),end="")
    spaces=spaces-1
    str=string[0:letter]
    letter=letter+1
    print(str)
    i=i+1


#Factorial 
print("-----FACTORIAL-----")
a= int(input("Enter range lower limit : "))
b= int(input("Enter range upper limit : "))
fact=1

def factorial (number):
	if number==0:
		return 1

	if number==1:
		return number

	if number!=0:
		return number*factorial(number-1)


for i in range(a,b+1,1):
	print ("Factorial of ", i, " = ", factorial(i))


#Fibonacci 
print("-----FIBONACCI-----")
a= int(input("Enter no of terms : "))

def fibonacci (num):
	if num<=1:
		return num
	else:
		return (fibonacci(num-1)+fibonacci(num-2)) 
if a<=0:
	print("Enter positive")
else:
	for i in range(a):
		print (fibonacci(i), end = "\t")



