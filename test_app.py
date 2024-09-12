import pytest
from unittest.mock import patch
from app import calculate_top_spenders, get_request_data

# Test cases for calculate_top_spenders function

def test_customers_with_negative_or_zero_invoice_amounts():
    customers = [{"ID": 0, "name": "Alice", "surname": "Klark"}]
    invoices = [{"ID": 0, "customerId": 0, "amount": -50.00}, {"ID": 1, "customerId": 0, "amount": 0}]
    
    result = calculate_top_spenders(customers, invoices)
    assert result == []  # Should return an empty list if no valid spending

def test_duplicate_customers():
    customers = [
        {"ID": 0, "name": "Alice", "surname": "Klark"},
        {"ID": 0, "name": "Alice", "surname": "Klark"}
    ]
    invoices = [{"ID": 0, "customerId": 0, "amount": 100}]
    
    result = calculate_top_spenders(customers, invoices)
    assert result == [{"name": "Alice", "surname": "Klark", "total_spent": 100}]  # The duplicate should not affect the result

def test_multiple_customers_with_same_top_spending():
    """Test case where multiple customers have the same top spending amount."""
    # Define customer data
    customers = [
        {"ID": 0, "name": "Alice", "surname": "Klark"},
        {"ID": 1, "name": "Bob", "surname": "McAdoo"},
        {"ID": 2, "name": "Charlie", "surname": "Brown"}
    ]
    
    # Define invoice data where Alice and Bob both have the highest spending
    invoices = [
        {"ID": 0, "customerId": 0, "amount": 150},  # Alice spends 150
        {"ID": 1, "customerId": 1, "amount": 150},  # Bob spends 150
        {"ID": 2, "customerId": 2, "amount": 100}   # Charlie spends 100
    ]
    
    # Call the function to get top spenders
    result = calculate_top_spenders(customers, invoices)
    
    # Expected result: Alice and Bob both have the highest spending of 150
    expected_result = [
        {"name": "Alice", "surname": "Klark", "total_spent": 150.00},
        {"name": "Bob", "surname": "McAdoo", "total_spent": 150.00}
    ]
    
    # Assert that the result matches the expected result
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_invoices_with_non_existent_customer_ids():
    customers = [{"ID": 0, "name": "Alice", "surname": "Klark"}]
    invoices = [{"ID": 0, "customerId": 1, "amount": 100}]  # customerId 1 does not exist
    
    result = calculate_top_spenders(customers, invoices)
    assert result == []  # No valid invoices for existing customers

def test_customers_without_names_or_surnames():
    customers = [{"ID": 0, "name": "", "surname": ""}]
    invoices = [{"ID": 0, "customerId": 0, "amount": 100}]
    
    result = calculate_top_spenders(customers, invoices)
    assert result == [{"name": "", "surname": "", "total_spent": 100.00}]  # Empty strings for name and surname should still return total

def test_customers_with_very_large_invoice_amounts():
    customers = [{"ID": 0, "name": "Alice", "surname": "Klark"}]
    invoices = [{"ID": 0, "customerId": 0, "amount": 1e10}]  # Very large amount
    
    result = calculate_top_spenders(customers, invoices)
    assert result == [{"name": "Alice", "surname": "Klark", "total_spent": 1e10}]  # Should handle very large invoice amounts

def test_empty_strings_for_customer_names_or_surnames():
    customers = [{"ID": 0, "name": "", "surname": ""}]
    invoices = [{"ID": 0, "customerId": 0, "amount": 100}]
    
    result = calculate_top_spenders(customers, invoices)
    assert result == [{"name": "", "surname": "", "total_spent": 100.00}]  # Should handle empty name and surname strings