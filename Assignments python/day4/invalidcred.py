data = {
		"Kriti":"9876",
		"Sayon":"1234",
		"Vinay":"ape1",
		"Gogi":"at12",
		"Ashmita":"4567"
}

class InvalidCred(Exception):
	def __init__(self,msg="Credentials mismatched!"):
		Exception.__init__(self,msg)

try:
	name=input("Enter Username: ")
	psw=input("Enter Password: ")
	
	if name in data and psw==data[name]:
		print("Welcome ")
		
	else:
		raise InvalidCred 

except InvalidCred as e:
	print(e)