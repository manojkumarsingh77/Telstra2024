from azure.storage.blob import BlobServiceClient
import os

connect_str = "your_connection_string"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name = "cdr-archive"

# Upload file
local_file_name = "sample_cdr.csv"
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

with open(local_file_name, "rb") as data:
    blob_client.upload_blob(data)
    print(f"{local_file_name} uploaded to Blob Storage.")
