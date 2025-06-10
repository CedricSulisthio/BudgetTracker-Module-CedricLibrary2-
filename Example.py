from CedricLibrary2 import BudgetTracker

tracker = BudgetTracker()

# Add categories
tracker.add_category("Groceries")
tracker.add_category("Entertainment")

# Add transactions
tracker.add_transaction("Groceries", -50.00)
tracker.add_transaction("Entertainment", -20.00)

# Generate report
report = tracker.generate_report()
print(report)