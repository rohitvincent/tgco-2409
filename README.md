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

# THE CHALLENGE

Write an application that calculates which customer spent the most money in our store and displays his/her name, surname, and total amount spent.

# EXTRA POINTS

What is the best test strategy for an application like this? The team with the best test strategy will be awarded 5 extra points!

Tip: No, "I will let QA decide" is not an option

# EVEN MORE EXTRA POINTS

The team with highest test coverage will be awarded 5 extra points!

# PYTHON SETUP
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
```bash
python app.py
```

Top Spender details can be found at http://127.0.0.1:5000/top-spender

# TESTING
Run the following command to run unit-tests:
```bash
pytest
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




