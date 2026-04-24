from expense_manager import (
    validate_date, validate_category, validate_amount,
    add_expense, monthly_summary, VALID_CATEGORIES
)
from logger import view_logs, log_error

def menu():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Logs")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            # Date validation make supre proper date entered
            date = input("Enter date (DD-MM-YYYY): ").strip()
            if not validate_date(date):
                print("Invalid date format. Use DD-MM-YYYY.")
                log_error("Invalid date entered.")
                continue

            # Category validation we have only "Food", "Travel", "Bills", "Entertainment", "Others" categories
            category = input(f"Enter category {VALID_CATEGORIES}: ").strip()
            if not validate_category(category):
                print(f"Invalid category. Choose from: {VALID_CATEGORIES}")
                log_error("Invalid category entered.")
                continue

            # Amount validation
            amount_str = input("Enter amount: ").strip()
            if not validate_amount(amount_str):
                print("Invalid amount. Must be a positive number.")
                log_error("Invalid amount entered.")
                continue
            amount = float(amount_str)

            description = input("Enter description: ").strip()
            add_expense(date, category, amount, description)

        elif choice == "2":
            # Month/year validation
            try:
                month = int(input("Enter month (1-12): ").strip())
                year = int(input("Enter year (YYYY): ").strip())
                if month < 1 or month > 12 :
                    raise ValueError
                monthly_summary(month, year)
            except ValueError:
                print("Enter valid month (1-12) and year (YYYY).")
                log_error("Invalid month/year entered.")

        elif choice == "3":
            view_logs()

        elif choice == "4":
            print("Thank you")
            break

        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
        menu()

