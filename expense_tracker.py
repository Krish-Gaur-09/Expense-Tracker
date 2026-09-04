# Expense Tracker Project

expensesList = [] #List of expenses in form of dictionary
print("\n")
print(" Welcome to Expense Tracker 🙏: \n")

while True:
    print("====MENU====")
    print(" PRESS 1 TO ADD EXPENSES")
    print(" PRESS 2 TO VIEW ALL EXPENSES")
    print(" PRESS 3 TO VIEW TOTAL AMOUNT")
    print(" PRESS 4 TO DELETE EXPENSE")
    print(" PRESS 5 TO UPDATE EXPENSE")
    print(" PRESS 6 TO EXIT\n")

    choice = int(input("Enter your choice: "))

#1. ADD EXPENSES
    if(choice==1):
        date=input("Enter money spending date (ex-> 01 January 2000): ")
        category=input("Enter category (ex-> Food, Travel, Clothes etc): ")
        description=input("Enter description: ")
        amount=float(input("Enter amount: "))

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
                print(f"Spending number {count} -> {eachSpending['date']}, {eachSpending['category']}, {eachSpending['description']}, {eachSpending['amount']}")
                count+=1

        print("\n")

#3. VIEW TOTAL SPENDING
    elif(choice==3):
        Total=0
        for eachSpending in expensesList:
            Total = Total + eachSpending["amount"]

        print("Total Spending: ",Total)
        print("\n")

    
#4. DELETE EXPENSES
    elif(choice==4):
        del_expense=int(input("Enter expense number which you want to delete: "))
        if(del_expense >=1 and del_expense <= len(expensesList)):
            deleted_expense = expensesList.pop(del_expense-1)
            print("Deleted expense :", deleted_expense)
            print("\n")
        else:
            print("wrong Expense number ❌\n")


#5. UPDATE EXPENSES
    elif(choice==5):
        update_expense = int(input("Enter Expense number which you want to update: "))
        if(update_expense >=1 and update_expense <=len(expensesList)):
            print("What do you want to update ?\n1. date\n2. category\n3. description\n4. amount\n")
            num=int(input("Enter your number: "))
            selected_expense = expensesList[update_expense - 1]
            if(num==1):
                selected_expense["date"]=input("Enter new date: ")
                print("Date is updated successfully.\n")
            elif(num==2):
                selected_expense["category"]=input("Enter new Category: ")
                print("Category is updated successfully.\n")
            elif(num==3):
                selected_expense["description"]=input("Enter new description: ")
                print("Description is updated successfully.\n")
            elif(num==4):
                selected_expense["amount"]=float(input("Enter new amount: "))
                print("Amount is updated successfully.\n")
            else:
                print("Invalid number ❌\n")
        else:
            print("Wrong Expense Number ❌\n")


#6. EXIT
    elif(choice==6):
        print("Thanks For using our system 🙏\n")
        break

    else:
        print("INVALID NUMBER. TRY AGAIN 🔄️\n")
