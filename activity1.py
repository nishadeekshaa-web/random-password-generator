import datetime
transactions = []
balance = 0.0
def add_transaction(t_type, amount, category, description):
    global balance
    if amount <= 0: return
    transactions.append({
        'date': datetime.date.today(), 'type': t_type, 
        'amount': amount, 'category': category, 'description': description
    })
    balance += amount if t_type == 'Income' else -amount
    print(f"✅ {t_type} added.") #
def view_transactions():
    for t in transactions:
        print(f"[{t['date']}] {t['type']}: {t['amount']} ({t['category']})")
def main_menu():
    while True:
        print("\n--- Finance Tracker ---\n1. Add Inc/Exp\n2. View\n3. Balance\n4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            t_type = input("Type (Income/Expense): ")
            amt = float(input("Amount: "))
            add_transaction(t_type, amt, input("Category: "), "Desc")
        elif choice == '2': view_transactions()
        elif choice == '3': print(f"Balance: {balance}") #
        elif choice == '4': break
if __name__ == "__main__": main_menu()