
## Prerequisites

Ensure you have Docker installed on your system. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

## Setup Instructions

1. **Clone the repository** (if applicable) or download the project files to your local machine.

2. **Navigate to the project directory**:

   ```bash
   cd imdb_scraper

3. **Build the Docker image**:
    ```bash
    docker build -t scrapy-flask-app .

4. **Run the Docker Container**:
    ```bash
    docker run -p 5000:5000 scrapy-flask-app

5. **Access the flask app**:
    Open your web browser and navigate to http://localhost:5001/movies to view the data served by the Flask application.

    You can also use curl to access the API:
    ```bash
    curl http://localhost:5001/movies
    ```
# Deploying a Kubernetes Deployment on AWS EKS

This guide will walk you through the steps to deploy a `deployment.yaml` file on an AWS EKS (Elastic Kubernetes Service) cluster.

## Prerequisites

1. **AWS Account**: Ensure you have an active AWS account.
2. **AWS CLI**: Install the AWS Command Line Interface (CLI). [Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
3. **kubectl**: Install `kubectl`, the Kubernetes command-line tool. [Installation Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
4. **eksctl**: Install `eksctl`, a CLI for EKS. [Installation Guide](https://eksctl.io/introduction/#installation)

## Steps

### Step 1: Configure AWS CLI

Ensure that your AWS CLI is configured with the necessary credentials:

    ```bash
    aws configure
    ```

### Step 2: Create an EKS Cluster
Use eksctl to create a new EKS cluster:

    ```bash
    eksctl create cluster --name <your-cluster-name> --region <your-region> --nodegroup-name <your-node-group-name> --node-type t3.medium --nodes 3
    Replace <your-cluster-name>, <your-region>, and <your-node-group-name> with your desired values.
    ```

### Step 3: Update kubeconfig
Update your kubeconfig file to use the new EKS cluster:

    ```bash
    aws eks --region <your-region> update-kubeconfig --name <your-cluster-name>
    ```

### Step 4: Verify Cluster
Ensure your cluster is up and running:

    ```bash
    kubectl get nodes
    ```

You should see a list of nodes indicating that your cluster is ready.

### Step 5: Deploy Your Application
Apply your deployment.yaml file to your EKS cluster:

    ```bash
    kubectl apply -f deployment.yaml
    ```

### Step 6: Verify Deployment
Check the status of your deployment and pods:

    ```bash
    kubectl get deployments
    kubectl get pods
    ```

### Step 7: Verify Service
Check the status of your service:

    ```bash
    kubectl get services
    ```

### Step 8: Verify Ingress
Check the status of your ingress:

    ```bash
    kubectl get ingress
    ```

### Step 9: Access Your Application
Retrieve the external IP or hostname of the ingress to access your application. You might need to update your DNS records to point to this IP or hostname:

    ```bash
    kubectl get ingress
    Use the external IP or hostname to access your application at http://dummy-domain.com/scrapy.
    ```


This `README.md` file includes the project structure, setup instructions, and all the necessary code and configurations to get your project up and running. If you need further assistance, feel free to ask!

