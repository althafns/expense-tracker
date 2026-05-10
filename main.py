import csv

list_expense  = []

try:
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if not row:
                continue
            
            expense = {
                "amount": int(row[0]),
                "category": row[1],
                "desc": row[2]
            }
            list_expense.append(expense)
            

except FileNotFoundError:
    pass

def add_expenses(expenses):
    price = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    expense = {
        "amount":price,
        "category":category,
        "desc":description
    }
    expenses.append(expense)
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([price, category, description])
    

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet")
        return
    total = 0
    for exp in expenses:
        print(f'{exp["category"]} | ₹{exp["amount"]} | {exp["desc"]}')
        total = total + exp["amount"]
    print("Total expenses:\n", total)

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete")
        return

    for i, exp in enumerate(expenses):
        print(i, "|", exp["category"], "|", exp["amount"], "|", exp["desc"])

    index = int(input("Enter expense index to delete: "))
    expenses.pop(index)

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for exp in expenses:
            writer.writerow([exp["amount"], exp["category"], exp["desc"]])

    print("Expense deleted \n")
    print("After deleting")
    view_expenses(list_expense)

def search_expense(expenses):
    category = input("Enter category to search: ")
    found = False

    for exp in expenses:
        if exp["category"] == category:
            print(f'{exp["category"]} | ₹{exp["amount"]} | {exp["desc"]}')
            found = True

    if not found:
        print("Category not found\n")

while(True):
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    print("4. Delete Expense")
    print("5. Search Expense")

    choose = int(input("Enter the corresponding number to choose: "))

    if(choose == 1):
        add_expenses(list_expense)
    elif(choose == 2):
        view_expenses(list_expense)
    elif(choose == 3):
        print("Exiting...")
        break
    elif(choose == 4):
        delete_expense(list_expense)
    elif(choose == 5):
        search_expense(list_expense)
    else:
        print("Invalid number")

