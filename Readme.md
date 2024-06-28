
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
# For running the application on AWS EKS.

Run the `aws-deployment.yaml` file in cluster.

---
This `README.md` file includes the project structure, setup instructions, and all the necessary code and configurations to get your project up and running. If you need further assistance, feel free to ask!

