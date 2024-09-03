
# Exercise 1: Create an Azure Function App in Python

# This part of the exercise is done in the Azure portal by setting up an Azure Function App.

# Exercise 2: Connect Azure Function to Azure SQL Database

import pyodbc
import os

def connect_to_azure_sql():
    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    username = os.getenv('SQL_USERNAME')
    password = os.getenv('SQL_PASSWORD')
    
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    connection = pyodbc.connect(connection_string)
    
    return connection

def retrieve_customer_data():
    connection = connect_to_azure_sql()
    cursor = connection.cursor()
    cursor.execute("SELECT CustomerID, Email, Phone, NotificationPreference FROM Customers WHERE BillingCycle = CURRENT_DATE")
    customers = cursor.fetchall()
    
    return [{"CustomerID": row[0], "Email": row[1], "Phone": row[2], "NotificationPreference": row[3]} for row in customers]

# Exercise 3: Process Customer Data and Send Notifications

import requests

def send_notification(customer):
    if customer['NotificationPreference'] == 'Email':
        send_email(customer)
    elif customer['NotificationPreference'] == 'SMS':
        send_sms(customer)

def send_email(customer):
    api_key = os.getenv('SENDGRID_API_KEY')
    url = 'https://api.sendgrid.com/v3/mail/send'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    data = {
        "personalizations": [{
            "to": [{"email": customer['Email']}],
            "subject": "Your Monthly Bill"
        }],
        "from": {"email": "noreply@telecom.com"},
        "content": [{"type": "text/plain", "value": f"Dear Customer {customer['CustomerID']}, your bill has been generated."}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code

def send_sms(customer):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_phone = os.getenv('TWILIO_PHONE_NUMBER')
    to_phone = customer['Phone']
    
    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    data = {
        "From": from_phone,
        "To": to_phone,
        "Body": f"Dear Customer {customer['CustomerID']}, your bill has been generated."
    }
    response = requests.post(url, auth=(account_sid, auth_token), data=data)
    return response.status_code

# Exercise 4: Parameterize the Azure Function

def main(req):
    customer_id = req.params.get('CustomerID')
    notification_type = req.params.get('NotificationType')
    
    customers = retrieve_customer_data()
    
    for customer in customers:
        if customer['CustomerID'] == customer_id and customer['NotificationPreference'] == notification_type:
            send_notification(customer)
    
    return f"Notification sent to Customer {customer_id} via {notification_type}"

# Exercise 5: Deploy and Monitor the Azure Function

# This part of the exercise involves deploying the function and setting up monitoring in the Azure portal.
