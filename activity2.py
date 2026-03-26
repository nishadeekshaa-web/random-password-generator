import datetime
transactions = []
def add_transaction():
    """Prompts the user for transaction details and adds it to the list."""
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        trans_type = input("Enter type (income/expense): ").lower()
        if trans_type not in ['income', 'expense']:
            print("Invalid type. Please enter 'income' or 'expense'.")
            return
        category = input("Enter category (e.g., Food, Salary, Travel, Other): ")
        date = datetime.date.today().isoformat()
        transaction = {
            'amount': amount,
            'type': trans_type,
            'category': category,
            'date': date
        }
        transactions.append(transaction)
        print("Transaction added successfully.")
    except ValueError:
        print("Invalid input. Please enter a numerical amount.")
def view_transactions():
    """Displays all recorded transactions."""
    if not transactions:
        print("No transactions recorded yet.")
        return
    print("\n--- Transaction History ---")
    for trans in transactions:
        print(f"Date: {trans['date']} | Type: {trans['type'].capitalize()} | Category: {trans['category']} | Amount: ${trans['amount']:.2f}")
    print("---------------------------\n")
def calculate_summary():
    """Calculates and displays the total income, expenses, and remaining balance."""
    total_income = sum(trans['amount'] for trans in transactions if trans['type'] == 'income')
    total_expenses = sum(trans['amount'] for trans in transactions if trans['type'] == 'expense')
    balance = total_income - total_expenses
    print("\n--- Financial Summary ---")
    print(f"Total Income:  ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Current Balance: ${balance:.2f}")
    print("-------------------------\n")
def main():
    """Main function to run the bank app interface."""
    while True:
        print("\n===== Bank App Menu =====")
        print("1. Add a transaction")
        print("2. View all transactions")
        print("3. View financial summary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            calculate_summary()
        elif choice == '4':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()