import os

# Initialize budget variables
income = 0
expenses = []


# Function to input income
def enter_income():
    global income
    try:
        income = float(input("Enter your income: $"))
        print("Income entered successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid income.")


# Function to enter expenses
def enter_expense():
    global expenses
    category = input("Enter expense category: ")
    try:
        amount = float(input(f"Enter expense amount for {category}: $"))
        expenses.append({"category": category, "amount": amount})
        print(f"Expense for {category} entered successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")


# Function to calculate remaining budget
def calculate_budget():
    global income, expenses
    total_expenses = sum(item["amount"] for item in expenses)
    remaining_budget = income - total_expenses
    return remaining_budget


# Function to display expense analysis
def display_expense_analysis():
    global expenses
    categories = set(item["category"] for item in expenses)
    print("Expense Analysis:")
    for category in categories:
        total_category_expense = sum(item["amount"] for item in expenses if item["category"] == category)
        print(f"{category}: ${total_category_expense:.2f}")


# Function to save data to a file
def save_data():
    global income, expenses
    with open("budget_data.txt", "w") as file:
        file.write(f"Income: {income}\n")
        for expense in expenses:
            file.write(f"Expense: {expense['category']}, Amount: {expense['amount']}\n")
    print("Data saved successfully.")


# Main loop
while True:

    print("Console-Based Budget Tracker")
    print("1. Enter Income")
    print("2. Enter Expense")
    print("3. Calculate Remaining Budget")
    print("4. Display Expense Analysis")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        enter_income()
    elif choice == "2":
        enter_expense()
    elif choice == "3":
        remaining_budget = calculate_budget()
        print(f"Remaining Budget: ${remaining_budget:.2f}")
    elif choice == "4":
        display_expense_analysis()
    elif choice == "5":
        save_data()
    elif choice == "6":
        print("Exiting Budget Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

    input("Press Enter to continue...")
