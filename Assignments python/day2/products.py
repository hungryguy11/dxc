choice = int(input("1.Sort by Cost (L-H)\n"
                   "2.Sort by Cost (H-L)\n"
                   "3.Sort by Rating\n"
                   "4.Sort by Discount (L-H)\n"
                   "5.Sort by Discount (H-L)\n"))



products = [
    {
        "pid":1,
        "name":"A1",
        "cost":15000,
        "brand":"Lenovo",
        "category":"Mobiles",
        "rating":3,
        "discount":65
    },
{
        "pid":2,
        "name":"A2",
        "cost":22500,
        "brand":"Lenovo",
        "category":"Mobiles",
        "rating":4,
        "discount":52
    },
{
        "pid":3,
        "name":"B1",
        "cost":18000,
        "brand":"Samsung",
        "category":"Mobiles",
        "rating":2,
        "discount":60
    },
{
        "pid":4,
        "name":"B2",
        "cost":12500,
        "brand":"Samsung",
        "category":"Mobiles",
        "rating":3,
        "discount":40
    },
{
        "pid":5,
        "name":"C1",
        "cost":45500,
        "brand":"Samsung",
        "category":"TV",
        "rating":4,
        "discount":35
    },
{
        "pid":5,
        "name":"C3",
        "cost":43000,
        "brand":"LG",
        "category":"TV",
        "rating":4,
        "discount":35
    },
{
        "pid":6,
        "name":"C3",
        "cost":38000,
        "brand":"Sony",
        "category":"TV",
        "rating":3,
        "discount":40
    },
{
        "pid":7,
        "name":"D1",
        "cost":11000,
        "brand":"JBL",
        "category":"Speaker",
        "rating":1,
        "discount":40
    },
{
        "pid":8,
        "name":"D2",
        "cost":8000,
        "brand":"Sony",
        "category":"Speaker",
        "rating":3,
        "discount":51
    },
{
        "pid":9,
        "name":"E1",
        "cost":82000,
        "brand":"HP",
        "category":"Laptop",
        "rating":5,
        "discount":47
    },
{
        "pid":10,
        "name":"E1",
        "cost":56000,
        "brand":"ASUS",
        "category":"Laptop",
        "rating":4,
        "discount":51
    }

]

print (type(products))

#sort
sorttype =[["cost",False],["cost",True],["rating",True],["discount",False],["discount",True]]



products.sort(key = lambda ele: ele[sorttype[choice-1][0]], reverse=sorttype[choice-1][1])


print("Name"    ,"Cost"    ,"Brand"   ,"Category"  ,"Rating" ,"Discount",sep="\t\t")
for i in products:
    print(i["name"],"    ",i["cost"],"    ",i["brand"],"    ",i["category"],"             ",i["rating"],"     ",i["discount"],sep="\t")	
		
#filter
choice2 = int(input("1.Filter by Name\n"
                         "2.Filter by Brand\n"
                         "3.Filter by Category\n"))
filtertype =["name","brand","category"]

string = input("Enter : ")

newobj = filter(lambda ele: ele[filtertype[choice2-1]] == string,products)


print("Name    Cost    Brand   Category    Rating  Discount")   

for i in newobj:
    print(i["name"],"    ",i["cost"],"    ",i["brand"],"    ",i["category"],"    ",i["rating"],"    ",i["discount"],sep="\t")
	



		




