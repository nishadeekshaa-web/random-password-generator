import json
import os
DATA_FILE = 'finance_tracker_data.json'
def load_data():
    """Load data from file if it exists, otherwise return empty lists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'income': [], 'expenses': [], 'balance': 0.0}
def save_data(data):
    """Save data to a JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully.")
def add_transaction(data, type):
    """Add a new income or expense transaction."""
    try:
        amount = float(input(f"Enter {type} amount: "))
        description = input(f"Enter description for {type}: ")
        if amount <= 0:
            print("Amount must be positive.")
            return
        data[type].append({'amount': amount, 'description': description})
        if type == 'income':
            data['balance'] += amount
        else:
            data['balance'] -= amount
        print(f"{type.capitalize()} of {amount} recorded.")
    except ValueError:
        print("Invalid amount. Please enter a number.")
def view_summary(data):
    """Display a summary of all income, expenses, and current balance."""
    print("\n--- Financial Summary ---")
    print(f"Current Balance: {data['balance']:.2f}")
    print("\nIncome Records:")
    for item in data['income']:
        print(f"- {item['amount']:.2f}: {item['description']}")
    print("\nExpense Records:")
    for item in data['expenses']:
        print(f"- {item['amount']:.2f}: {item['description']}")
    print("-------------------------")
def main():
    """Main function to run the finance tracker application."""
    data = load_data()
    print("Welcome to the Python Finance Tracker!")
    while True:
        print("\nChoose an option:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_transaction(data, 'income')
        elif choice == '2':
            add_transaction(data, 'expenses')
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            save_data(data)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()