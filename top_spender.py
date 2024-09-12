def calculate_top_spender(customers: list, invoices: list) -> dict:
    """Calculates the top spender from the provided customers & invoices data and display the information."""
    if not (len(invoices) and len(customers)):
        print("Customers and Invoice data cannot be empty!")
        return None

    # Dictionary to store total amount spent by each customer
    customer_spending = {}

    # Calculate total spending for each customer
    for invoice in invoices:
        customer_id = invoice["customerId"]
        amount = invoice["amount"]

        if customer_id in customer_spending:
            customer_spending[customer_id] += amount
        else:
            customer_spending[customer_id] = amount

    # Find the customer ID who spent the most
    top_customer_id = max(customer_spending, key=customer_spending.get)
    total_amount_spent = customer_spending[top_customer_id]

    # Find the corresponding customer details and returns `None` if not found
    top_customer = next((cust for cust in customers if cust["ID"] == top_customer_id), None)

    if top_customer:
        # Display the name, surname, and total amount spent
        print("--------------------------------------------------------------")
        print(f"Top spender: {top_customer['name']} {top_customer['surname']}")
        print(f"Total amount spent: ${total_amount_spent:.2f}")
        print("--------------------------------------------------------------")
        top_customer.update({"total_spent": total_amount_spent})
        return top_customer
    else:
        print("Top spender not found")
        return None
