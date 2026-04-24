import csv

DATA_FILE = "expenses.csv"

def add_to_csv(date, category, amount, description):
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def load_from_csv():
    expenses = []
    try:
        with open(DATA_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header row
            for row in reader:
                if row:
                    expenses.append({
                        "date": row[0].strip(),
                        "category": row[1].strip(),
                        "amount": float(row[2].strip()),
                        "description": row[3].strip()
                    })
    except FileNotFoundError:
        pass
    return expenses


