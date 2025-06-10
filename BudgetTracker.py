import datetime

class BudgetTracker:
    def __init__(self):
        self.categories = {}  # Categories of expenses or incomes
        self.transactions = []  # List of transactions

    def add_category(self, category_name):
        """Add a new budget category (e.g., groceries, entertainment)."""
        self.categories[category_name] = 0

    def add_transaction(self, category, amount, date=None):
        """Add a transaction under a given category (either income or expense)."""
        if date is None:
            date = datetime.date.today()
        if category not in self.categories:
            raise ValueError(f"Category {category} does not exist.")
        transaction = {"category": category, "amount": amount, "date": date}
        self.transactions.append(transaction)
        self.categories[category] += amount

    def get_balance(self):
        """Get the total balance across all categories."""
        return sum([transaction["amount"] for transaction in self.transactions])

    def get_category_balance(self, category):
        """Get the total balance for a specific category."""
        return self.categories.get(category, 0)

    def generate_report(self):
        """Generate a summary report of the budget tracker."""
        report = {}
        for category, balance in self.categories.items():
            report[category] = balance
        return report