import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import os

# Set environment variables for blob storage
STORAGE_CONNECTION_STRING = os.getenv("AzureWebJobsStorage")
CONTAINER_NAME = 'csvcontainer'

app = func.FunctionApp()

@app.function_name(name="UploadCsvFunction")
@app.route(route="upload-csv")  # HTTP Trigger
def upload_csv_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Azure Function triggered to upload CSV to Blob Storage.')

    try:
        # Get the file from the request
        file = req.files['file']
    except KeyError:
        return func.HttpResponse("File not provided in the request.", status_code=400)

    if file:
        try:
            # Initialize BlobServiceClient using the connection string
            blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)

            # Get a reference to the container and blob client
            blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.filename)

            # Upload the file to blob storage
            blob_client.upload_blob(file.stream.read(), overwrite=True)

            logging.info(f"File '{file.filename}' uploaded successfully.")
            return func.HttpResponse(f"File '{file.filename}' uploaded to Blob Storage.", status_code=200)

        except Exception as e:
            logging.error(f"Error uploading file to Blob Storage: {str(e)}")
            return func.HttpResponse(f"Error: {str(e)}", status_code=500)
    else:
        return func.HttpResponse("No file provided.", status_code=400)
