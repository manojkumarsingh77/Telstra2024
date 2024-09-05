import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import os

# Define the environment variable for the connection string
CONNECTION_STRING = os.getenv("AzureWebJobsStorage")
BLOB_CONTAINER_NAME = "csv-container"  # Update with your container name

# Define the function using the function decorator
app = func.FunctionApp()

@app.function_name(name="BlobUploadFunction")
@app.route(route="upload", methods=["POST"])
def upload_to_blob(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('BlobUploadFunction triggered.')

    try:
        # Get file data from the request
        file_data = req.get_body()
        file_name = req.params.get('file_name', 'default.txt')

        # Create the BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

        # Access the container and upload the file
        container_client = blob_service_client.get_container_client(BLOB_CONTAINER_NAME)
        blob_client = container_client.get_blob_client(file_name)

        # Upload the file data
        blob_client.upload_blob(file_data, overwrite=True)

        return func.HttpResponse(f"File {file_name} uploaded successfully.", status_code=200)

    except Exception as e:
        logging.error(f"Error uploading file: {e}")
        return func.HttpResponse(f"Failed to upload file: {str(e)}", status_code=500)
