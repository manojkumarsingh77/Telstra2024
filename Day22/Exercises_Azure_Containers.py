Exercise 1: Telecom User Metrics Dashboard

Objective:
Develop a Python Flask application that serves telecom user statistics and deploy it on Azure Cloud using containers.

Step-by-Step Instructions:
Create the Flask Application:
Create a directory for your project and add the following app.py:
python
Copy code
from flask import Flask, jsonify

app = Flask(__name__)

telecom_data = {
    "total_users": 100000,
    "active_users": 90000,
    "average_call_duration": 3.5,
    "network_availability": "99.8%"
}

@app.route('/')
def dashboard():
    return jsonify(telecom_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
Create requirements.txt:

            List the dependencies:

Flask==2.0.1

            Create the Dockerfile:
This will build the container image:
dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]

            Build the Docker Image:

docker build -t telecom-metrics-dashboard .

            Test the Image Locally:

docker run -p 8080:8080 telecom-metrics-dashboard

            Push Image to Azure Container Registry:
Create ACR:

az acr create --resource-group <your-resource-group> --name <your-acr-name> --sku Basic
Push image:

docker tag telecom-metrics-dashboard <your-acr-name>.azurecr.io/telecom-metrics-dashboard:latest
docker push <your-acr-name>.azurecr.io/telecom-metrics-dashboard:latest

            Deploy to Azure Container Instance (ACI):

            
az container create \
--resource-group <your-resource-group> \
--name telecom-metrics-instance \
--image <your-acr-name>.azurecr.io/telecom-metrics-dashboard:latest \
--dns-name-label telecom-metrics-app \
--ports 8080

            Access the Web App:

http://<telecom-metrics-app>.<region>.azurecontainer.io:8080

            Summary:
You created a dashboard displaying telecom user statistics, containerized the app, pushed it to ACR, and deployed it on ACI. The app is accessible via a public DNS URL.

Exercise 2: Telecom Call Drop Rate Analyzer

Objective:
Develop a web app to analyze telecom call drop rates and deploy it using containers on Azure Cloud.

Step-by-Step Instructions:
Create the Flask Application:

from flask import Flask, jsonify

app = Flask(__name__)

call_drop_data = {
    "region_1": 0.02,
    "region_2": 0.05,
    "region_3": 0.03,
    "region_4": 0.01
}

@app.route('/call-drop-rate')
def call_drop_rate():
    return jsonify(call_drop_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

            Dockerfile:
dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]

            Build the Docker Image:

docker build -t telecom-call-drop-analyzer .
Push the Image to Azure Container Registry:

            Create ACR and push the image:

docker tag telecom-call-drop-analyzer <your-acr-name>.azurecr.io/telecom-call-drop-analyzer:latest
docker push <your-acr-name>.azurecr.io/telecom-call-drop-analyzer:latest

            Deploy to ACI:

az container create \
--resource-group <your-resource-group> \
--name telecom-call-drop-instance \
--image <your-acr-name>.azurecr.io/telecom-call-drop-analyzer:latest \
--dns-name-label telecom-call-drop-app \
--ports 8080

            Access the Web App:

http://<telecom-call-drop-app>.<region>.azurecontainer.io:8080/call-drop-rate

            Summary:
This exercise focused on analyzing call drop rates in different regions and deploying the web app to Azure using Docker and ACR.

Exercise 3: Telecom Data Usage Tracker

Objective:
Build and deploy a web app that tracks telecom data usage for different regions.

Step-by-Step Instructions:
Flask Application:

from flask import Flask, jsonify

app = Flask(__name__)

data_usage = {
    "region_1": 500,
    "region_2": 1200,
    "region_3": 800,
    "region_4": 950
}

@app.route('/data-usage')
def data_usage_tracker():
    return jsonify(data_usage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

                                              Dockerfile:
dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]

                                              Build Docker Image:

docker build -t telecom-data-usage-tracker .

                                              Push Image to ACR:

docker tag telecom-data-usage-tracker <your-acr-name>.azurecr.io/telecom-data-usage-tracker:latest
docker push <your-acr-name>.azurecr.io/telecom-data-usage-tracker:latest

                                              Deploy to ACI:

az container create \
--resource-group <your-resource-group> \
--name telecom-data-usage-instance \
--image <your-acr-name>.azurecr.io/telecom-data-usage-tracker:latest \
--dns-name-label telecom-data-usage-app \
--ports 8080

            Access the Web App:

http://<telecom-data-usage-app>.<region>.azurecontainer.io:8080/data-usage

            Summary:
In this exercise, you created a web app that tracks telecom data usage per region and deployed it to Azure via ACR and ACI.

Exercise 4: Telecom Network Coverage Map

Objective:
Develop a telecom network coverage tracker for regions and deploy it on Azure.

Step-by-Step Instructions:
Flask Application:

from flask import Flask, jsonify

app = Flask(__name__)

network_coverage = {
    "region_1": "98%",
    "region_2": "95%",
    "region_3": "90%",
    "region_4": "85%"
}

@app.route('/network-coverage')
def coverage():
    return jsonify(network_coverage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

                Dockerfile:
dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]

                Build Docker Image:

docker build -t telecom-network-coverage .
Push Image to ACR:
bash
Copy code
docker tag telecom-network-coverage <your-acr-name>.azurecr.io/telecom-network-coverage:latest
docker push <your-acr-name>.azurecr.io/telecom-network-coverage:latest

                Deploy to ACI:

az container create \
--resource-group <your-resource-group> \
--name telecom-coverage-instance \
--image <your-acr-name>.azurecr.io/telecom-network-coverage:latest \
--dns-name-label telecom-coverage-app \
--ports 8080

                Access the Web App:
                ]
http://<telecom-coverage-app>.<region>.azurecontainer.io:8080/network-coverage

                Summary:
This exercise demonstrates the creation of a web app for tracking telecom network coverage and its deployment to Azure.

Each of these exercises involves building a telecom-related web application, containerizing it, pushing it to Azure Container Registry, and deploying it via Azure Container Instance. You can now build your own services for telecom applications using these exercises!



Exercise 5: Telecom Performance Dashboard Deployment
Objective:
Build and deploy a Telecom Performance Dashboard that tracks KPIs such as active users, average data usage, network latency, and customer satisfaction. The dashboard will be developed using Python Flask and will be containerized, pushed to Azure Container Registry (ACR), and deployed on Azure Container Instance (ACI).

Step-by-Step Instructions:
Step 1: Build the Telecom Performance Dashboard Application

            Create a Project Directory:

mkdir telecom-performance-dashboard
cd telecom-performance-dashboard

            Create the app.py file: In this file, you will create a simple Flask application that will serve the performance metrics dashboard.

from flask import Flask, render_template
import random

app = Flask(__name__)

# Dummy performance metrics for the dashboard
def get_telecom_metrics():
    metrics = {
        "active_users": random.randint(200000, 500000),
        "average_data_usage": round(random.uniform(1.0, 10.0), 2),  # in GB
        "network_latency": random.randint(20, 100),  # in ms
        "customer_satisfaction": random.randint(60, 100)  # in percentage
    }
    return metrics

@app.route('/')
def dashboard():
    metrics = get_telecom_metrics()
    return render_template('dashboard.html', metrics=metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

            Create the templates Directory: Inside the project directory, create a folder named templates, which will hold the HTML file for rendering the dashboard.

mkdir templates
Create the dashboard.html Template: Inside the templates folder, create the dashboard.html file:
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Telecom Performance Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        .metric {
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
        }
        .metric h2 {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Telecom Performance Dashboard</h1>
    <div class="metric">
        <h2>Active Users</h2>
        <p>{{ metrics.active_users }} users</p>
    </div>
    <div class="metric">
        <h2>Average Data Usage</h2>
        <p>{{ metrics.average_data_usage }} GB</p>
    </div>
    <div class="metric">
        <h2>Network Latency</h2>
        <p>{{ metrics.network_latency }} ms</p>
    </div>
    <div class="metric">
        <h2>Customer Satisfaction</h2>
        <p>{{ metrics.customer_satisfaction }} %</p>
    </div>
</body>
</html>

            Step 2: Create the requirements.txt File
Create a requirements.txt file in the project directory to list the necessary dependencies for your Flask application.


Flask==2.0.1
Step 3: Create a Dockerfile to Containerize the Application
Create a Dockerfile in the project root with the following content:

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
Build the Docker Image: Run the following command to build your Docker image:

docker build -t telecom-performance-dashboard .
Test the Docker Image Locally: Run the Docker container locally to make sure everything works:

docker run -p 8080:8080 telecom-performance-dashboard
Open a browser and navigate to http://localhost:8080/ to see the Telecom Performance Dashboard.

            Step 4: Push the Image to Azure Container Registry (ACR)
Login to Azure (if not already logged in):

az login
Create an Azure Container Registry (ACR):

az acr create --resource-group <your-resource-group> --name <your-acr-name> --sku Basic
Tag the Docker Image: Tag the Docker image for pushing to the ACR:

docker tag telecom-performance-dashboard <your-acr-name>.azurecr.io/telecom-performance-dashboard:latest
Push the Docker Image to ACR: Push the tagged image to the ACR:

docker push <your-acr-name>.azurecr.io/telecom-performance-dashboard:latest

            Step 5: Deploy the Docker Image to Azure Container Instance (ACI)
Deploy the Container to ACI: Use the Azure CLI to deploy the container to Azure Container Instance:

az container create \
--resource-group <your-resource-group> \
--name telecom-performance-dashboard-instance \
--image <your-acr-name>.azurecr.io/telecom-performance-dashboard:latest \
--dns-name-label telecom-dashboard-app \
--ports 8080

            Verify the Deployment: Check the status of the container using the following command:

az container show --resource-group <your-resource-group> --name telecom-performance-dashboard-instance --query instanceView.state
Access the Dashboard: Once the container is running, you can access the Telecom Performance Dashboard by visiting the following URL:

http://<telecom-dashboard-app>.<region>.azurecontainer.io:8080/

            Exercise Summary:
In this exercise, you:

Built a Telecom Performance Dashboard using Python Flask.
Containerized the application using Docker.
Pushed the Docker image to Azure Container Registry.
Deployed the image to Azure Container Instance.
