!pip install azure-data-tables
from azure.data.tables import TableServiceClient, TableEntity

table_service = TableServiceClient.from_connection_string(connect_str)
table_client = table_service.get_table_client(table_name="ProductInventory")

# Sample data
products = [
    {"PartitionKey": "Product", "RowKey": "1", "product_name": "Product A", "quantity": 50},
    {"PartitionKey": "Product", "RowKey": "2", "product_name": "Product B", "quantity": 150},
    {"PartitionKey": "Product", "RowKey": "3", "product_name": "Product C", "quantity": 20},
]

for product in products:
    table_client.create_entity(entity=product)
