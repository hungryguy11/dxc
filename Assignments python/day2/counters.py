

def outer():
	
	counter=0
	def inner():
		nonlocal counter
		counter+= 1
		print(counter)
	return inner	

hello=outer()	
hello()  #count of hello = 1
hello()  #count of hello = 2
hi=outer()
hello()  #count of hello = 3
hello()  #count of hello = 4
hi()    #count of hi = 1
hi()    #count of hi= 2