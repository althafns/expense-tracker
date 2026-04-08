list_expense  = []

def add_expenses(expenses):
    expense = int(input("Enter the expense: "))
    expenses.append(expense)

def view_expenses(expenses):
    print("list of expense",expenses)
    print("total expenses: ",sum(expenses))

while(True):
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choose = int(input("Enter the corresponding number to choose: "))

    if(choose == 1):
        add_expenses(list_expense)
    elif(choose == 2):
        view_expenses(list_expense)
    elif(choose == 3):
        print("Exiting...")
        break
    else:
        print("Invalid number")

