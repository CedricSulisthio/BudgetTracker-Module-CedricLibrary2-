import unittest
from CedricLibrary2.BudgetTracker import BudgetTracker

class TestBudgetTracker(unittest.TestCase):

    def test_add_category(self):
        tracker = BudgetTracker()
        tracker.add_category("Groceries")
        self.assertIn("Groceries", tracker.categories)

    def test_add_transaction(self):
        tracker = BudgetTracker()
        tracker.add_category("Groceries")
        tracker.add_transaction("Groceries", -50.00)
        self.assertEqual(tracker.get_category_balance("Groceries"), -50.00)

    def test_generate_report(self):
        tracker = BudgetTracker()
        tracker.add_category("Groceries")
        tracker.add_transaction("Groceries", -50.00)
        tracker.add_category("Rent")
        tracker.add_transaction("Rent", -500.00)
        report = tracker.generate_report()
        self.assertEqual(report["Groceries"], -50.00)
        self.assertEqual(report["Rent"], -500.00)