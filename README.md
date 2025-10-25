
# Flask App with Docker

This guide walks you through creating a simple Flask application, containerizing it with Docker, and deploying it to Docker Hub.

---

## 🧩 Steps

### 1. Create a Flask Project
Create a new Flask project with a file named **server.py** inside your project directory.

---

### 2. Create a Dockerfile
Inside your project, create a folder named **Dockerfile** and add the Docker build instructions and a **dockerignore** file.

---

### 3. Create a Docker Hub Account
Sign up or log in to [Docker Hub](https://hub.docker.com/).

---

### 4. Build the Docker Image
Navigate to your project directory (where **server.py** is located) and open **Git Bash**.  
Run the following command to create the Docker image:

<pre>
docker build -t nasriladaa/test-flask:v1 .
</pre>
---

### 5. View All Created Images
List all images available on your local system:

<pre>docker images</pre>


### 6. Push the Image to Docker Hub
Push your image to your [Docker Hub repository](https://hub.docker.com/r/nasriladaa/test-flask):

<pre>docker push nasriladaa/test-flask:v1</pre>


### 7. Pull and Run the Image on Another Machine
From any machine with Docker installed, pull the image and run it on a specific port (for example 8085):

<pre>docker run --rm -it -p 8085:5000 nasriladaa/test-flask:v1</pre>


### 8.1 View Containers
View running containers:

<pre>docker ps</pre>



### 8.2 View all containers (including stopped ones):

<pre>docker ps -a</pre>


### 9. Delete a Specific Image
To delete a Docker image from your local system:

<pre>docker rmi firstimg:latest</pre>


## 🛠️ Tools

It is preferable to download and install the following tools:

  - Docker Desktop (for managing containers and images)

  - VS Code Docker Extension (for integrated Docker support in Visual Studio Code)
