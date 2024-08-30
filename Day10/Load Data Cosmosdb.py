!pip install azure-cosmos

endpoint = "YOUR_COSMOS_DB_ENDPOINT"
primary_key = "YOUR_COSMOS_DB_PRIMARY_KEY"

from azure.cosmos import CosmosClient, PartitionKey, exceptions
import json

# Initialize the Cosmos client
client = CosmosClient(endpoint, primary_key)

# Create a database if it does not exist
database_name = 'ProductCatalogDB'
database = client.create_database_if_not_exists(id=database_name)

# Create a container if it does not exist
container_name = 'Products'
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/category"),
    offer_throughput=400
)

# Load product catalog data from JSON (assuming data is already loaded into the `product_catalog` variable)
product_catalog = [
    # Include the JSON data from above here
]

# Insert items into the container
for product in product_catalog:
    try:
        container.create_item(body=product)
        print(f"Inserted {product['product_name']}")
    except exceptions.CosmosResourceExistsError:
        print(f"{product['product_name']} already exists")
