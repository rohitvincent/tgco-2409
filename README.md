# PREREQUISITS
## Install Node
    - https://nodejs.org/en/learn/getting-started/how-to-install-nodejs
    - https://www.geeksforgeeks.org/installation-of-node-js-on-windows/

# RUN THE "REMOTE" SERVICES
node invoices.js
node node customers.js

# CONNECT TO THE "REMOTE" SERVICES

Customer service can be reached at GET httP://localhost:9000

Invoce service can be reached at GET http://localhost:9092

# WHAT THE "REMOTE" SERVICES RETURN

Custor service returns data about customers. For Example:

```
    "customers": [
        {
            "ID": 0,
            "name": "Alice",
            "surname": "Klark"
        },
```

where ID is the unique identifier and name and surname are the name and the surname of our customer.

Invoice service returns data about invoices. For exampls:

```
{
    "invoices": [
        {
            "ID": 0,
            "customerId": 0,
            "amount": 12
        },
```

where ID is the unique identifier, customer ID is the customer ID, which is loosely coupled with the Customer data, and the amount is the amount that our customer has been charged.

If we assume that Alice Klark has one invoce only then her total amount spent would be 12.

# THE CHALLENGE
write an application that calculates which customer spent more money in our store and displays his/her name, surname and total amount spent.