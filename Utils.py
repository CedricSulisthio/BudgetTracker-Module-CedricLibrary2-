import csv

def save_to_csv(transactions, filename="transactions.csv"):
    """Save transactions to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date"])
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)