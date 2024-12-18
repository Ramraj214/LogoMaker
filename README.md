# Logo Maker Application

This is a Logo Maker application that leverages a Hugging Face Black Forest AI model to generate logos based on user input. The backend is built with Python using FastAPI, and the frontend is developed using HTML, CSS, and JavaScript.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Install Backend Dependencies](#install-backend-dependencies)
  - [Set Up Frontend](#set-up-frontend)
- [Backend Routes](#backend-routes)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
  - [Docker Setup](#docker-setup)
  - [AWS EC2 (Optional)](#aws-ec2-optional)
  - [Jenkins (Optional)](#jenkins-optional)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Users can input text and other requirements for their desired logo.
- The application generates logos using an AI model (Hugging Face Black Forest).
- FastAPI backend for efficient logo generation.
- Simple HTML/CSS/JS frontend for a smooth user experience.

## Technologies Used
- **Backend**: Python, FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: Hugging Face Black Forest
- **Database**: MongoDB
- **Deployment**: Docker, AWS EC2, Jenkins

## Setup and Installation

### Prerequisites
- Python 3.x
- Docker (for containerized deployment)
- Git
- AWS EC2 (optional, for cloud deployment)
- MongoDB (local or cloud instance)
- Docker Hub or any container registry (optional for image storage)

### Clone the Repository
bash
git clone https://github.com/your-username/logo-maker-app.git
cd logo-maker-app

### Navigate to the backend directory:
bash
cd backend

### Install required Python packages:
bash
pip install -r requirements.txt

## Set Up Frontend

### Navigate to the frontend directory:
bash
cd frontend

Ensure that the necessary HTML, CSS, and JS files are present.

## Backend Routes
### POST /signup
This route allows users to sign up by providing a username, email, and password.

Request Parameters:
{
username: User's chosen username.
email: User's email address.
password: User's password.
}

Response:
200 OK if signup is successful.
400 Bad Request if username or email already exists.

### POST /login
This route allows users to log in using their username or email and password.

Request Body:
json
{
  "identifier": "username_or_email",
  "password": "user_password"
}

Response:
200 OK if login is successful.
401 Unauthorized if login credentials are invalid.

### POST /generate
This route generates a logo based on user input. The prompt text is passed to the Hugging Face Black Forest AI model to generate a logo.

Request Body:
json
{
  "username": "user_username",
  "prompt": "Logo design for a tech company"
}

Response:
200 OK with a success message and the generated image's filename.
404 Not Found if the user does not exist.

Functionality:
The backend uses the Hugging Face API to generate a logo based on the provided prompt.
The generated image is saved locally and associated with the user in the database.
The prompt and image name are stored in MongoDB for record-keeping.

### POST /signup
Generates a new user account.

Example Request:
bash
curl -X 'POST' \
  'http://<EC2-Public-IP>:5000/signup?username=JohnDoe&email=john@example.com&password=mysecretpassword' \
  -H 'accept: application/json'
POST /login
Logs in an existing user.

Example Request:
bash
curl -X 'POST' \
  'http://<EC2-Public-IP>:5000/login' \
  -H 'accept: application/json' \
  -d '{
    "identifier": "JohnDoe",
    "password": "mysecretpassword"
}'

### POST /generate
Generates a logo based on the user input.

Example Request:
bash
curl -X 'POST' \
  'http://<EC2-Public-IP>:5000/generate' \
  -H 'accept: application/json' \
  -d '{
    "username": "JohnDoe",
    "prompt": "Logo design for a tech startup"
}'

## Deployment
### Docker Setup
#### Build Docker Images:

For the backend:
bash
docker build -t backend-app ./backend

For the frontend:
bash
docker build -t frontend-app ./frontend

#### Run the Containers:

bash
docker run -d --name frontend-container -p 3000:3000 frontend-app

docker run -d --name backend-container -p 5000:5000 backend-app

## AWS EC2 (Optional)
You can deploy the application on AWS EC2. Ensure that your EC2 security group allows traffic on ports 3000 (frontend) and 5000 (backend).

## Jenkins (Optional)
You can automate the build and deployment using Jenkins. Please refer to the Jenkinsfile for pipeline configuration.

## Usage
Open the application in your browser: http://<EC2-IP>:3000
Enter the logo name, color scheme, and style in the frontend form.
The backend will process the input, generate a logo, and send it back to the frontend.
Contributing

## We welcome contributions! To contribute:
- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Make your changes
- Commit your changes (git commit -am 'Add new feature')
- Push to the branch (git push origin feature-branch)
- Create a new pull request
  
## License
This project is licensed under the Apache License - see the LICENSE file for details.
