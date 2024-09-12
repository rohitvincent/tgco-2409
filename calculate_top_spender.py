import requests
import argparse

# Sample customers and invoices data
customers = [
    {"ID": 0, "name": "Alice", "surname": "Klark"},
    {"ID": 1, "name": "Bob", "surname": "McAdoo"},
    {"ID": 2, "name": "Cindy", "surname": "Law"},
    {"ID": 3, "name": "David", "surname": "Nap"},
    {"ID": 4, "name": "Elvis", "surname": "Blue"}
]

invoices = [
    {"ID": 0, "customerId": 0, "amount": 12.00},
    {"ID": 1, "customerId": 0, "amount": 235.78},
    {"ID": 2, "customerId": 1, "amount": 5.060},
    {"ID": 3, "customerId": 2, "amount": 12.60},
    {"ID": 4, "customerId": 3, "amount": 0.99},
    {"ID": 5, "customerId": 1, "amount": 12.00},
    {"ID": 6, "customerId": 1, "amount": 235.78},
    {"ID": 7, "customerId": 1, "amount": 5.060},
    {"ID": 8, "customerId": 1, "amount": 12.60},
    {"ID": 9, "customerId": 1, "amount": 0.99},
    {"ID": 10, "customerId": 3, "amount": 12.00},
    {"ID": 11, "customerId": 2, "amount": 235.78},
    {"ID": 12, "customerId": 1, "amount": 5.060},
    {"ID": 13, "customerId": 0, "amount": 12.60},
    {"ID": 15, "customerId": 3, "amount": 0.99}
]

def get_request_data(url):
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        # If the request failed, print the status code and error message
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(f"Error message: {response.text}")
        return None


def calculate_top_spender(customers:list, invoices:list) -> dict:
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


if __name__ == '__main__':

    # Create the parser
    parser = argparse.ArgumentParser(description="Application to calculate which customer spent the most money in the store and displays his/her name, surname, and total amount spent.")

    # Add arguments
    parser.add_argument('--use_remote_data', type=bool, required=True, default=True, help='Whether to use remote customers & invoice data.')
    parser.add_argument('--customer_data_url', required=False, type=str, default="http://localhost:9090/", help='customer data endpoint(default :"http://localhost:9090/")')
    parser.add_argument('--invoice_data_url', required=False, type=str, default="http://localhost:9092/", help='invoice data endpoint(default :"http://localhost:9092/")')

    # Parse all arguments including the dynamically added ones
    args = parser.parse_args()

    # Dynamically add arguments based on the `use_remote_data`
    if args.use_remote_data:
        use_remote_data = True
    else:
        use_remote_data = False

    # Use remote data
    if use_remote_data:
        customer_data_url = args.customer_data_url
        invoice_data_url = args.invoice_data_url

        # Retrieve the customer data
        customers_data = get_request_data(customer_data_url)
        # If data was successfully retrieved, assign it to the 'customers' variable
        if customers_data and 'customers' in customers_data:
            customers = customers_data['customers']
            print("Customer Data Retrieved Successfully:")
        else:
            print("No customer data available or an error occurred.")

        # Retrieve the invoice data
        invoice_data = get_request_data(invoice_data_url)
        # If data was successfully retrieved, assign it to the 'invoices' variable
        if invoice_data and 'invoices' in invoice_data:
            invoices = invoice_data['invoices']
            print("Invoice Data Retrieved Successfully:")
        else:
            print("No invoice data available or an error occurred.")

    # Call the function
    calculate_top_spender(customers, invoices)
