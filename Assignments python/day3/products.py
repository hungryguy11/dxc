import operator
class Product :
	sorttype = [["cost",False],["cost",True],["rating",True],["discount",False],["discount",True]]
	filtertype =["name","brand","category"]
	def __init__(self,pid,name,cost,brand,category,rating,discount):
		self.pid=pid
		self.name=name
		self.cost=cost
		self.brand=brand
		self.category=category
		self.rating=rating
		self.discount=discount

	# def create():
	# 	num = int(input("Enter no of products "))
	# 	pList = []
	# 	for i in range(0,num):
	# 		pid = int(input("Enter Id : "))
	# 		name = input("Enter Name : ")
	# 		cost = int(input("Enter Cost : "))
	# 		brand = input("Enter Brand : ")
	# 		category = input ("Enter Category : ")
	# 		rating = int(input("Enter Rating : " ))
	# 		discount = int(input("Enter Discount : "))
	# 		p = Product(pid,name,cost,brand,category,rating,discount)
	# 		pList.append(p)
	# 		print("-----Next-----")

	# 	return pList

	def view(pList):
		print("ID", "Name","Cost","Brand","Category","Rating","Discount",sep = "\t")
		for i in pList:

		
			print(i.pid, i.name, i.cost,i.brand,i.category,"     ",i.rating,i.discount,sep = "\t")

p=Product(pid = 1,
    name= "A1",
    cost=15000,
    brand="Lenovo",
    category="Mobiles",
    rating=3,
    discount=65)
p1 = Product(pid = 2,
    name= "A2",
    cost=18000,
    brand="Menovo",
    category="Mobiles",
    rating=8,
    discount=85)
p2 = Product(3,"E3",2000,"LG","Toaster",4,60)
p3 = Product(4,"E4",5600,"Samsung","Toaster",7,100)


# spList=Product.create()
spList=[p,p1,p2,p3]




choice = int(input("1.Sort by Cost (L-H)\n"
                   "2.Sort by Cost (H-L)\n"
                   "3.Sort by Rating\n"
                   "4.Sort by Discount (L-H)\n"
                   "5.Sort by Discount (H-L)\n"))
sorttype = [["cost",False],["cost",True],["rating",True],["discount",False],["discount",True]]

# print( Product.sorttype[choice-1][0] , Product.sorttype[choice-1][1])
# sortkey = operator.attrgetter('sorttype')
# print(sortkey(Product))

spList.sort(key = lambda ele : getattr(ele,sorttype[choice-1][0]), reverse=Product.sorttype[choice-1][1])

Product.view(spList)


choice = int(input("1.Filter by Name \n2.Filter by Brand\n3.Filter by Category\n"))
string = input("Enter : ")

newobj = filter(lambda ele:  ele.__getattribute__(Product.filtertype[choice-1]) == string, spList)

Product.view(newobj)

