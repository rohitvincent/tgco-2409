def calculate_top_spenders(customers, invoices):
    """Function to calculate the top spenders based on customer and invoice data"""
    customer_spending = {}

    for invoice in invoices:
        customer_id = invoice.get("customerId")
        amount = invoice.get("amount", 0)  # Default to 0 if amount is missing

        if customer_id is not None and amount > 0:  # Ignore negative amounts
            if customer_id in customer_spending:
                customer_spending[customer_id] += amount
            else:
                customer_spending[customer_id] = amount

    if not customer_spending:
        return []  # No spending data

    # Find the maximum spending amount
    max_spending = max(customer_spending.values())

    # Find all customers with the maximum spending amount
    top_spenders_ids = {
        cust_id
        for cust_id, amount in customer_spending.items()
        if amount == max_spending
    }

    # Get details of top spenders ensuring no duplicate based on first and last name
    seen_names = set()
    top_spender_details = []

    for cust in customers:
        if cust["ID"] in top_spenders_ids:
            name_key = (cust["name"], cust["surname"])
            if name_key not in seen_names:
                seen_names.add(name_key)
                top_spender_details.append({
                    "name": cust["name"],
                    "surname": cust["surname"],
                    "total_spent": max_spending
                })

    return top_spender_details
