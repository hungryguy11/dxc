def wallet(balance):
    print("New wallet : ")
    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        print("Rs",amount, " added to wallet. New Balance: Rs", balance)

    def spent(amount):
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            print("Rs",amount, " deducted from wallet. New Balance: Rs", balance)
        else:
            print("Insufficient Balance")

    def transfer(wal, amount):
        print("Fund Transfer of Rs.",amount," initiated : ")
        nonlocal balance
        if amount <= balance:
            balance = balance - amount
            dic = wal
            dic["deposit"](amount)
            print("Rs",amount, " deducted from wallet. New Balance: Rs", balance)

    def show():
        print("Available Balance: Rs", balance)
    #li = [deposit, spent, show]  #list of functions
    li = {"deposit": deposit, "spent": spent, "show": show, "transfer": transfer}    #dict of functions
    return li


l1=wallet(1000)
l1["show"]()
l1["deposit"](400)
l1["spent"](200)
l1["show"]()

l2=wallet(2000)
l2["show"]()


l1["transfer"](l2,500)


l1["show"]
l2["show"]

