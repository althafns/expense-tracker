list_expense  = []

while(True):
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choose = int(input("Enter the corresponding number to choose: "))

    if(choose == 1):
        expense = int(input("Enter the expense"))
        list_expense.append(expense)
    elif(choose == 2):
        print("list of expense",list_expense)
        print("total expenses: ",sum(list_expense))
    elif(choose == 3):
        print("Exiting...")
        break
    else:
        print("Invalid number")

