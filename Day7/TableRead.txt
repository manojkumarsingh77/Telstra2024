import pandas as pd
import plotly.express as px
from azure.data.tables import TableServiceClient

# Connect to Azure Table Storage
connect_str = "your_connection_string"
table_service = TableServiceClient.from_connection_string(connect_str)
table_client = table_service.get_table_client(table_name="ProductInventory")

# Query entities with low stock
entities = table_client.query_entities("quantity lt 50")
data = [entity for entity in entities]

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Visualize the data
fig = px.bar(df, x='product_name', y='quantity', title='Low Stock Products')
fig.show()
