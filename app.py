from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Remote services URLs
CUSTOMER_DATA_URL = "http://localhost:9090/"
INVOICE_DATA_URL = "http://localhost:9092/"

def get_request_data(url):
    """Function to make GET request and return data"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any unsuccessful status code
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

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

@app.route('/top-spender', methods=['GET'])
def get_top_spenders():
    # Retrieve customers and invoices data
    customers_data = get_request_data(CUSTOMER_DATA_URL)
    invoices_data = get_request_data(INVOICE_DATA_URL)

    if not customers_data or not invoices_data:
        return jsonify({"error": "Failed to fetch customer or invoice data"}), 500

    customers = customers_data.get("customers", [])
    invoices = invoices_data.get("invoices", [])

    # Calculate top spenders
    top_spenders = calculate_top_spenders(customers, invoices)

    if top_spenders:
        # Return the top spenders' details in JSON format
        return jsonify(top_spenders)
    else:
        return jsonify({"error": "No spending data found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
