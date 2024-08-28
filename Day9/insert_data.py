import pyodbc
import time

# Azure SQL Database connection details
server = '<your-server-name>.database.windows.net'
database = '<your-database-name>'
username = '<your-username>'
password = '<your-password>'

# Create the connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish a connection
conn = pyodbc.connect(conn_str)

# Function to insert data into the Customers table
def insert_data():
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, RegistrationDate, Status)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    data = ('John', 'Doe', 'john.doe@example.com', '1234567890', '2024-08-28', 'Active')
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()

# Function to run the insert_data function every 30 seconds
def run_cron_job():
    while True:
        insert_data()
        print("Data inserted successfully!")
        time.sleep(30)

if __name__ == "__main__":
    run_cron_job()
