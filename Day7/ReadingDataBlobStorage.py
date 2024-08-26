!pip install azure-storage-blob pandas plotly

from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import plotly.express as px

# Replace with your Azure Blob Storage connection string and container name
connect_str = "azure connectionstring"
container_name = "cdr-archive"
blob_name = "cdr_data_202408.csv"  # Name of the file in the blob

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Read the blob content into a pandas DataFrame
stream = io.BytesIO(blob_client.download_blob().readall())
df = pd.read_csv(stream)

# Display the DataFrame
df.head()

# Example visualization: Bar chart of call durations by caller ID
fig = px.bar(df, x='caller_id', y='call_duration', title='Call Duration by Caller ID')
fig.show()
