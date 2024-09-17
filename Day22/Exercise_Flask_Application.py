Exercise: Deploy a Telecom Dashboard Application Using Docker, Azure Container Registry, and Azure Container Instance
Objective:

Build a simple Python-based telecom dashboard web app (using Flask) to display telecom data.
Package it into a Docker container locally.
Push the Docker image to Azure Container Registry (ACR).
Deploy the container to Azure Container Instance (ACI).
Prerequisites:

Docker installed locally.
Python and Flask installed locally.
An active Azure subscription.
Azure CLI installed locally.
Step 1: Build a Simple Telecom Dashboard Web App
Create a simple Python Flask app that serves a telecom dashboard. This app will be containerized and deployed.

Create a Project Directory:
bash
Copy code
mkdir telecom-dashboard
cd telecom-dashboard
Create a Python Virtual Environment (optional but recommended):
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Flask:
bash
Copy code
pip install Flask
Create the app.py file: Create a file named app.py and add the following content:
python
Copy code
from flask import Flask, jsonify

app = Flask(__name__)

# Telecom data (dummy data)
telecom_data = {
    "total_users": 500000,
    "active_users": 450000,
    "call_drop_rate": 0.05,
    "network_coverage": "99.5%"
}

@app.route('/')
def index():
    return jsonify(telecom_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
Create a requirements.txt file: This will list the dependencies needed for your application. Add the following line:
bash
Copy code
Flask==2.0.2
Step 2: Create a Dockerfile
To containerize the Flask application, create a Dockerfile in the same project directory with the following content:

dockerfile
Copy code
# Use the official Python image from DockerHub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application to the container
COPY . .

# Expose port 8080 to the host
EXPOSE 8080

# Set the entry point to run the app
CMD ["python", "app.py"]
Step 3: Build and Test the Docker Image Locally
Build the Docker Image: In the terminal, run the following command to build your Docker image:
bash
Copy code
docker build -t telecom-dashboard:latest .
Run the Docker Container Locally: Test the app by running the Docker container:
bash
Copy code
docker run -p 8080:8080 telecom-dashboard:latest
Access the App: Open a browser and go to http://localhost:8080. You should see a JSON response with the telecom data.
Step 4: Push the Docker Image to Azure Container Registry (ACR)
Login to Azure: If not already logged in, use the Azure CLI to log in:
bash
Copy code
az login
Create an Azure Container Registry (ACR): Replace <your-resource-group> and <your-registry-name> with your own values:
bash
Copy code
az acr create --resource-group <your-resource-group> --name <your-registry-name> --sku Basic
Login to the Container Registry:
bash
Copy code
az acr login --name <your-registry-name>
Tag the Docker Image: Tag the image so that it can be pushed to the ACR:
bash
Copy code
docker tag telecom-dashboard:latest <your-registry-name>.azurecr.io/telecom-dashboard:latest
Push the Docker Image to ACR: Push the tagged image to your Azure Container Registry:
bash
Copy code
docker push <your-registry-name>.azurecr.io/telecom-dashboard:latest
Step 5: Deploy the Docker Image to Azure Container Instance (ACI)
Deploy the Container to Azure: Run the following command to deploy your Docker container to Azure Container Instance:
bash
Copy code
az container create \
--resource-group <your-resource-group> \
--name telecom-dashboard-instance \
--image <your-registry-name>.azurecr.io/telecom-dashboard:latest \
--registry-login-server <your-registry-name>.azurecr.io \
--registry-username <your-registry-username> \
--registry-password <your-registry-password> \
--dns-name-label telecom-dashboard-app \
--ports 8080
Check the Deployment: Run the following command to check the status of your container:
bash
Copy code
az container show --resource-group <your-resource-group> --name telecom-dashboard-instance --query instanceView.state
Access the App: Once the container is running, you can access the app by visiting the DNS name assigned to the container:
bash
Copy code
http://<telecom-dashboard-app>.<region>.azurecontainer.io:8080
Exercise Summary:
You created a Python Flask app to simulate a telecom dashboard.
You packaged the app into a Docker container.
You pushed the container to Azure Container Registry.
You deployed the app to Azure Container Instance and accessed it via a public URL.
