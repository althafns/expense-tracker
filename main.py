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
    print("Total expenses:", total)

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

