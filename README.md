# Flask CI/CD Pipeline using Jenkins and Docker
 
## Project Overview
 
This project demonstrates a complete CI/CD pipeline using:
 
- Python Flask
- Jenkins
- Docker
- GitHub
- Pytest
 
## Pipeline Stages
 
1. Checkout Source Code
2. Build Docker Image
3. Install Dependencies
4. Run Automated Tests
5. Deploy Application
 
## Run Locally
 
```bash
pip install -r requirements.txt
python app.py
```
 
## Build Docker Image
 
```bash
docker build -t flask-demo .
```
 
## Run Container
 
```bash
docker run -d -p 5000:5000 flask-demo
```
 
## Jenkins
 
Configure a Pipeline Job and point it to the repository Jenkinsfile.