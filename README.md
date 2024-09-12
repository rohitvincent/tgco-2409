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

```
python app.py
```

Top Spender details can be found at http://127.0.0.1:5000/top-spender

# Running Tests
```bash
pytest
```



