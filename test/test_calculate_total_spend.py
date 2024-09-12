import unittest
from calculate_top_spender import calculate_top_spender

class TestCalculateTopSpender(unittest.TestCase):
    def setUp(self):
        # Common customer data
        self.customers = [
            {"ID": 1, "name": "Alice", "surname": "Smith"},
            {"ID": 2, "name": "Bob", "surname": "Johnson"},
            {"ID": 3, "name": "Charlie", "surname": "Williams"},
        ]

    def test_single_invoice(self):
        invoices = [{"customerId": 1, "amount": 100.00}]
        expected = {"ID": 1, "name": "Alice", "surname": "Smith", "total_spent": 100.00}
        result = calculate_top_spender(self.customers, invoices)
        self.assertEqual(result, expected)

    def test_multiple_customers(self):
        invoices = [
            {"customerId": 1, "amount": 50.00},
            {"customerId": 2, "amount": 150.00},
            {"customerId": 3, "amount": 100.00}
        ]
        expected = {"ID": 2, "name": "Bob", "surname": "Johnson", "total_spent": 150.00}
        result = calculate_top_spender(self.customers, invoices)
        self.assertEqual(result, expected)

    def test_customer_with_no_match(self):
        # Invoice for a customer not in the customer list
        invoices = [{"customerId": 4, "amount": 200.00}]
        result = calculate_top_spender(self.customers, invoices)
        self.assertIsNone(result)

    def test_no_invoices(self):
        # No invoices at all
        invoices = []
        result = calculate_top_spender(self.customers, invoices)
        self.assertIsNone(result)

    def test_tied_spenders(self):
        invoices = [
            {"customerId": 1, "amount": 100.00},
            {"customerId": 2, "amount": 100.00},
            {"customerId": 3, "amount": 50.00}
        ]
        # In case of a tie, the max function would select the first customer with the max amount
        expected = {"ID": 1, "name": "Alice", "surname": "Smith", "total_spent": 100.00}
        result = calculate_top_spender(self.customers, invoices)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
