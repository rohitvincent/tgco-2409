# PREREQUISITS
## Install Node
    - https://nodejs.org/en/learn/getting-started/how-to-install-nodejs
    - https://www.geeksforgeeks.org/installation-of-node-js-on-windows/

# RUN THE "REMOTE" SERVICES

Run these in separate terminals
```
node invoices.js
```
```
node customers.js
```

# CONNECT TO THE "REMOTE" SERVICES

Customer service can be reached at GET http://localhost:9090

Invoice service can be reached at GET http://localhost:9092

# WHAT THE "REMOTE" SERVICES RETURN

The Customer service returns data about customers. For Example:

```
{
    "customers": [
        {
            "ID": 0,
            "name": "Alice",
            "surname": "Klark"
        },
        ...
    ]
}
```

where ID is the unique identifier and name and surname are the name and the surname of our customer.

The Invoice service returns data about invoices. For exampls:

```
{
    "invoices": [
        {
            "ID": 0,
            "customerId": 0,
            "amount": 12
        },
        ...
    ]
}
```

where ID is the unique identifier, customer ID is the customer ID, which is loosely coupled with the Customer data, and the amount is the amount that our customer has been charged.

If we assume that Alice Klark has one invoice only then her total amount spent would be 12.

# Python setup
## Install python
We recommend using python 3.11 or above. Download from [here](https://www.python.org/downloads/)

## Create a Virtual environment

We recommend using GitBash on Windows.
```bash
python -m venv .venv
source .venv/Scripts/activate
```
## Install dependencies
From the top-level directory enter the command to install pip and the dependencies of the project

```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

# Running the script
To see all the options available, use `-h`
```bash
$ python calculate_top_spender.py -h
usage: calculate_top_spender.py [-h] [--use_remote_data USE_REMOTE_DATA] [--customer_data_url CUSTOMER_DATA_URL] [--invoice_data_url INVOICE_DATA_URL]

Application to calculate which customer spent the most money in the store and displays his/her name, surname, and total amount spent.

options:
  -h, --help            show this help message and exit
  --use_remote_data USE_REMOTE_DATA
                        Whether to use remote customers & invoice data.
  --customer_data_url CUSTOMER_DATA_URL
                        customer data endpoint(default :"http://localhost:9090/")
  --invoice_data_url INVOICE_DATA_URL
                        invoice data endpoint(default :"http://localhost:9092/")
```

## Execute the scripts
```bash
# To work with local data
python calculate_top_spender.py --use_remote_data False

# To work with remote data(uses default endpoints for customer & invoice data when not provided )
python calculate_top_spender.py --use_remote_data True

# Explicitly provide endpoints urls
python calculate_top_spender.py --use_remote_data True --customer_data_url "http://localhost:9090" --invoice_data_url "http://localhost:9092"

```
## Frontend App

Run the backend Flask API:
```
python app.py
```

Top Spender details can be found at http://127.0.0.1:5000/top-spender

If you want a UI, run the streamlit app after deploy the Flask backend as per above:
```
streamlit run streamlit_app.py
```

# TESTING
Run the following command to run unit-tests:
```bash
pytest --cov=top_spender test_app.py --cov-report=term-missing
```

The following cases are covered as part of the unit test:
- **Test customers with negative or zero invoice amounts**
  *Checks if customers with invalid (negative or zero) invoice amounts are handled correctly and excluded from top spenders.*

- **Test duplicate customers**
  *Ensures that duplicate customer entries do not affect the results.*

- **Test multiple customers with the same top spending amount**
  *Validates that multiple customers with the same total spending are included as top spenders.*

- **Test invoices with non-existent customer IDs**
  *Tests how the function handles invoices with customer IDs that do not exist in the customer data.*

- **Test customers without names or surnames**
  *Checks if customers with empty names or surnames are still processed correctly.*

- **Test customers with very large invoice amounts**
  *Verifies that very large invoice amounts are handled properly.*

- **Test empty strings for customer names or surnames**
  *Ensures the function can handle customers with empty name or surname fields.*

- **Test malformed data from remote services**
  *Checks if the function gracefully handles missing or malformed invoice data, such as missing `customerId`.*

- **Test multiple customers with the same total spending**
  *Confirms that multiple customers with equal total spending are both recognized as top spenders.*

- **Test no invoices for any customers**
  *Verifies that if no invoices exist, no top spenders are returned.*

- **Test no customers**
  *Tests how the function handles the absence of customers, even if invoices are present.*

- **Test no invoices**
  *Checks the behavior when customers exist but there are no invoices.*

- **Test customers with multiple invoices**
  *Ensures that the total spent by a customer is the sum of all their invoices.*

- **Test customers without invoices**
  *Verifies that customers without invoices are excluded from the top spenders list.*

- **Test empty responses from services**
  *Ensures that the function correctly handles empty data for both customers and invoices.*

-**Test case where invoice has invalid customerId type**
  *Ensures that the function correctly handles invalid customer IDs.*

-**Test case where customer has invalid name types (non-string)**
*Ensures that the function correctly handles invalid customer Names.*

# TESTING STRATEGY

## 1. Unit Testing
Unit testing focuses on validating individual functions and components in isolation. For the Top Spender application, the main focus is on the `calculate_top_spenders()` and `get_request_data()` functions, ensuring they behave as expected under various conditions.

### Tools:
- **pytest**: A powerful testing framework used to write and execute unit tests.
- **unittest.mock.patch**: Used to mock external dependencies during testing, particularly for mocking the behavior of HTTP requests.

### Test Cases:
- **Positive Tests**: Validate the correct behavior of functions with normal, expected inputs.
- **Negative Tests**: Ensure functions handle incorrect or unexpected inputs gracefully without crashing.

---

## 2. Integration Testing
Integration tests validate that the different components of the application (Flask API, remote services) work together as expected. This includes making sure the application can retrieve and process data from remote customer and invoice services.

### Tools:
- **pytest with mocking**: Used to mock external HTTP requests to ensure the app can work with data fetched remotely.

### Test Cases:
- Validate the correct integration of customer and invoice data.
- Ensure proper handling of failed remote service requests.

---

## 3. Edge Case Testing
Edge cases are unusual or extreme conditions that could cause failures or unexpected behavior. The test strategy ensures that these edge cases are thoroughly covered:

### Edge Cases:
- Handling of invalid invoice amounts (negative or zero).
- Duplicate customer entries.
- Multiple customers with the same total spending.
- Invoices referencing non-existent customer IDs.
- Missing or malformed data from remote services.
- Handling very large invoice amounts.
- Customers with missing or empty fields.

---

## 4. Functional Testing
Functional tests ensure that the system behaves as expected from an end-user perspective. This involves testing the Flask API endpoints (`/top-spender`) and verifying the output format.

### Tools:
- **Postman or curl**: Can be used to simulate HTTP requests and validate responses from the API.
- **Flask's built-in testing client**: To simulate requests and capture responses programmatically.

---

## 5. User Interface Testing (Streamlit App)
If using the optional UI, it is important to verify the interaction between the frontend (Streamlit) and the backend Flask API. This ensures that the top spenders are displayed correctly.

### Tools:
- **Streamlit’s testing capabilities** to simulate interaction with the frontend components.

---

## 6. Performance Testing (Optional)
For large datasets, performance testing can ensure that the system scales effectively and responds within acceptable time limits. This may involve testing the application with large customer and invoice datasets to validate speed and memory usage.




