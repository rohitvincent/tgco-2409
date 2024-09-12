from flask import Flask, jsonify, redirect, url_for
import requests
from top_spender import calculate_top_spenders

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

@app.route('/', methods=['GET'])
def index():
    """Default route that redirects to the top spenders endpoint"""
    return redirect(url_for('get_top_spenders'))

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
