balance=0
transaction=[]
while True:
    print("1.add income")
    print("2.add expense")
    print("3.show balance")
    print("4.show transaction")
    print("5.Exit")
    choice=input("choose an option:")
    if choice=="1":
        amount=float(input("enter income amount:"))
        balance+=amount
        transaction.insert(0,("Income", amount))
        print("income added")
    elif choice=="2":
        amount= float(input("enter expense amount:"))
        balance-=amount
        transaction.insert(0,("Expense",amount))
        print("expense added:")
    elif choice=="3":
        print("current balanace:" ,balance)   
    elif choice=="4":
        for trans in transaction:
            print("transaction history:",transaction)
    elif choice=="5":
        print("Goodbye!")
        break
    else:
        print("invalid input")


