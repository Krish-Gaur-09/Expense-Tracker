# Expense Tracker Project

expensesList = [] #List of expenses in form of dictionary
print(" Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print(" PRESS 1 TO ADD EXPENSES")
    print(" PRESS 2 TO VIEW ALL EXPENSES")
    print(" PRESS 3 TO VIEW TOTAL AMOUNT")
    print(" PRESS 4 TO EXIT")

    choice = int(input("Enter your choice: "))

#1. ADD EXPENSES
    if(choice==1):
        date=input("Enter money spending date: ")
        category=input("Enter product's category (ex-> Food, Travel, Clothes etc): ")
        description=input("Enter product's description: ")
        amount=float(input("Enter product's amount: "))

        expense = {
            "date":date, 
            "category":category, 
            "description":description, 
            "amount":amount
        }
        
        expensesList.append(expense)
        print("Expense is added successfully 👍")
        print("\n")


#2. VIEW ALL EXPENSES
    elif(choice==2):
        if(len(expensesList)==0):
            print("No Expenses Added ❌")

        else:
            print("====These are your all expenses====")
            count = 1
            for eachSpending in expensesList:
                print(f"Spending number {count} -> {eachSpending["date"]}, {eachSpending["category"]}, {eachSpending["description"]}, {eachSpending["amount"]}")
                count+=1

        print("\n")

#3. VIEW TOTAL SPENDING
    elif(choice==3):
        Total=0
        for eachSpending in expensesList:
            Total = Total + eachSpending["amount"]

        print("Total Spending: ",Total)
        print("\n")

#4. EXIT
    elif(choice==4):
        print("Thanks For using our system 🙏 ")
        print("\n")
        break

    else:
        print("INVALID NUMBER. TRY AGAIN 🔄️")
        print("\n")
    