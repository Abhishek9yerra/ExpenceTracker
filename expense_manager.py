import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
from handler import add_to_csv, load_from_csv
from logger import log_info, log_error, log_warning

VALID_CATEGORIES = ["Food", "Travel", "Bills", "Entertainment", "Others"]

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validate_category(category):
    return category in VALID_CATEGORIES

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        return amount > 0
    except ValueError:
        return False

def add_expense(date, category, amount, description):
    add_to_csv(date, category, amount, description)
    log_info(f"Added expense: {date}, {category}, {amount}, {description}")
    print("Expense added successfully!")

def monthly_summary(month, year):
    expenses = load_from_csv()
    monthly_expenses = [
        e for e in expenses
        if datetime.datetime.strptime(e["date"], "%d-%m-%Y").month == month
        and datetime.datetime.strptime(e["date"], "%d-%m-%Y").year == year
    ]

    if not monthly_expenses:
        print("No expenses found for this month.")
        log_warning(f"No expenses found for {month}-{year}")
        return

    total = sum(e["amount"] for e in monthly_expenses)
    category_totals = defaultdict(float)
    for e in monthly_expenses:
        category_totals[e["category"]] += e["amount"]

    highest_category = max(category_totals, key=category_totals.get)

    print(f"\nMonthly Summary ({month}-{year})")
    print(f"Total Expenses: {total}")
    print(f"Highest Spending Category: {highest_category} ({category_totals[highest_category]})")

    log_info(f"Viewed summary for {month}-{year}: Total={total}, Highest={highest_category}")

    # Charts
    plt.bar(category_totals.keys(), category_totals.values(), color="skyblue")
    plt.title(f"Monthly Expenses {month}-{year}")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

    plt.pie(category_totals.values(), labels=category_totals.keys(), autopct="%1.1f%%")
    plt.title(f"Expense Breakdown {month}-{year}")
    plt.show()
