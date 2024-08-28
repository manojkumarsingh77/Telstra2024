# Make sure to keep CustomerID as BIGINT 
!pip install pymssql
import pymssql
import time
from datetime import datetime
import random

# Database connection parameters
server = 'unext-sqlserver.database.windows.net'
user = 'sqladminuser'
password = 'P@ssword1234'
database = 'unextdb'

# Function to connect to the database
def get_connection():
    return pymssql.connect(server=server, user=user, password=password, database=database)

# Function to insert unique records into the Customers and CustomerContacts tables
def insert_unique_record(conn):
    cursor = conn.cursor()

    # Generate smaller unique customer information
    customer_id = random.randint(1, 10**12)  # Generate a random integer within a safe BIGINT range
    first_name = f'FirstName_{customer_id}'
    last_name = f'LastName_{customer_id}'
    email = f'{first_name}.{last_name}@example.com'
    phone_number = f'123-456-789{customer_id % 10}'
    registration_date = datetime.now().strftime('%Y-%m-%d')

    # Insert into Customers table
    insert_customer_query = f"""
    INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber, RegistrationDate)
    VALUES ({customer_id}, '{first_name}', '{last_name}', '{email}', '{phone_number}', '{registration_date}')
    """
    cursor.execute(insert_customer_query)
    conn.commit()

    # Insert into CustomerContacts table
    contact_id = random.randint(1, 10**12)  # Generate a random integer within a safe BIGINT range
    contact_date = datetime.now().strftime('%Y-%m-%d')
    contact_type = 'Email'
    contact_description = f'Contact made via {contact_type} on {contact_date}'

    insert_contact_query = f"""
    INSERT INTO CustomerContacts (ContactID, CustomerID, ContactDate, ContactType, ContactDescription)
    VALUES ({contact_id}, {customer_id}, '{contact_date}', '{contact_type}', '{contact_description}')
    """
    cursor.execute(insert_contact_query)
    conn.commit()

    print(f"Inserted new records at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Main loop to insert records every 30 seconds
try:
    conn = get_connection()
    while True:
        insert_unique_record(conn)
        time.sleep(30)  # Wait for 30 seconds before inserting the next record
except KeyboardInterrupt:
    print("Script terminated by the user.")
finally:
    conn.close()
