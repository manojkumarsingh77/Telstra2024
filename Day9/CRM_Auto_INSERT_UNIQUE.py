!pip install pymssql
import pymssql
import time
from datetime import datetime, timedelta
import random

# Database connection parameters
server = 'unext-sqlserver.database.windows.net'
user = 'sqladminuser'
password = 'P@ssword1234'
database = 'unextdb'

# Function to connect to the database
def get_connection():
    return pymssql.connect(server=server, user=user, password=password, database=database)

# Function to generate random registration dates
def generate_registration_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime.now()
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate random contact dates
def generate_contact_date(registration_date):
    end_date = datetime.now()
    return registration_date + timedelta(days=random.randint(0, (end_date - registration_date).days))

# Function to insert unique records into the Customers and CustomerContacts tables
def insert_unique_record(conn):
    cursor = conn.cursor()

    # Generate unique customer information
    customer_id = random.randint(1, 10**6)  # Smaller range to avoid duplicates
    first_name = random.choice(['John', 'Jane', 'Michael', 'Sarah', 'Robert'])
    last_name = f'LastName_{customer_id}'
    email = f'{first_name}.{last_name}@example.com'
    phone_number = f'123-456-789{random.randint(0, 9)}'
    registration_date = generate_registration_date()

    # Insert into Customers table
    insert_customer_query = f"""
    INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber, RegistrationDate)
    VALUES ({customer_id}, '{first_name}', '{last_name}', '{email}', '{phone_number}', '{registration_date.strftime('%Y-%m-%d')}')
    """
    cursor.execute(insert_customer_query)
    conn.commit()

    # Insert multiple records into CustomerContacts table to ensure some customers have more than one contact
    contact_types = ['Email', 'Phone', 'In-Person']
    for _ in range(random.randint(1, 5)):  # 1 to 5 contacts per customer
        contact_id = random.randint(1, 10**6)
        contact_date = generate_contact_date(registration_date)
        contact_type = random.choice(contact_types)
        contact_description = f"Contact made via {contact_type} on {contact_date.strftime('%Y-%m-%d')}"
        
        # Add a few 'network issue' descriptions
        if random.random() < 0.2:  # 20% chance of 'network issue'
            contact_description = 'Reported network issue'

        insert_contact_query = f"""
        INSERT INTO CustomerContacts (ContactID, CustomerID, ContactDate, ContactType, ContactDescription)
        VALUES ({contact_id}, {customer_id}, '{contact_date.strftime('%Y-%m-%d')}', '{contact_type}', '{contact_description}')
        """
        cursor.execute(insert_contact_query)
        conn.commit()

    print(f"Inserted records for customer {customer_id} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Main loop to insert records every 30 seconds
try:
    conn = get_connection()
    for _ in range(10):  # Adjust the range to control the number of customers
        insert_unique_record(conn)
        time.sleep(2)  # Reduced sleep for faster insertion during testing
except KeyboardInterrupt:
    print("Script terminated by the user.")
finally:
    conn.close()
