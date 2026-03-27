# 🏋️ ACEest Fitness & Gym – CI/CD Pipeline Project

---

## 📌 Project Overview

This project demonstrates a complete **DevOps pipeline implementation** for a fitness application.
The application provides workout and diet plans for different fitness goals using a Flask-based API.

The project covers:

* Application Development
* Version Control
* Automated Testing
* Continuous Integration (CI)
* Containerization
* Build Automation

---

## 🎯 Objective

To design and implement a robust CI/CD pipeline that ensures:

* Code integrity
* Automated testing
* Environment consistency
* Reliable build validation

---

## 🛠️ Tech Stack

* **Backend**: Python (Flask)
* **Testing**: Pytest
* **Version Control**: Git & GitHub
* **CI Tool**: GitHub Actions
* **Containerization**: Docker
* **Build Tool**: Jenkins

---

## 📂 Project Structure

```
aceest-gym-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── tests/
│   └── test_app.py
│
└── .github/
    └── workflows/
        └── main.yml
```

---

## 🚀 Step-by-Step Implementation

---

## 🔹 1. Application Development (Flask)

A Flask API was developed to provide:

* Fitness programs (Fat Loss, Muscle Gain, Beginner)
* Workout plans
* Diet plans

### ▶️ Run Application

```bash
pip install flask
python app.py
```

Access in browser:

```
http://127.0.0.1:5000
```

---

## 🔹 2. Unit Testing using Pytest

Pytest was used to validate API functionality.

### ▶️ Install Pytest

```bash
pip install pytest
```

### ▶️ Run Tests

```bash
pytest
```

### ✔️ Output

```
4 passed
```

---

## 🔹 3. Version Control using Git & GitHub

Git was used to track code changes and GitHub was used as a remote repository.

### ▶️ Commands Used

```bash
git init
git add .
git commit -m "initial: flask app with pytest"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### ✔️ Purpose

* Maintain version history
* Enable collaboration
* Trigger CI/CD pipeline

---

## 🔹 4. Continuous Integration using GitHub Actions

GitHub Actions was used to automate testing on every code push.

### 📄 Workflow File

```
.github/workflows/main.yml
```

### ⚙️ Workflow Steps

* Trigger on push/pull request
* Install dependencies
* Run pytest
* Build Docker image

### ▶️ Workflow Code

```yaml
name: CI Pipeline

on:
  push:
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install flask pytest

    - name: Run tests
      run: |
        pytest

    - name: Build Docker Image
      run: |
        docker build -t aceest-gym-app .
```

### ✔️ Outcome

* Automated validation on every commit
* Ensures stable code

---

## 🔹 5. Containerization using Docker

Docker was used to package the application for consistent execution.

### 📄 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask pytest

EXPOSE 5000

CMD ["python", "app.py"]
```

---

### ▶️ Build Docker Image

```bash
docker build -t aceest-gym-app .
```

### ▶️ Run Container

```bash
docker run -p 5000:5000 aceest-gym-app
```

Access:

```
http://localhost:5000
```

---

## 🔹 6. Jenkins Build Automation

Jenkins was used as a secondary build validation tool.

---

### ⚙️ Jenkins Setup

```bash
docker run -p 8080:8080 -u root -v "<project-path>:/app" jenkins/jenkins:lts
```

Access:

```
http://localhost:8080
```

---

### ⚠️ Note

Due to network restrictions, plugins could not be installed.
Hence, the project was mounted directly into the Jenkins container.

---

### 🏗️ Job Configuration

* Job Type: Freestyle Project
* Source Code Management: None
* Build Step: Execute Shell

---

### ▶️ Build Script

```bash
cd /app

apt-get update
apt-get install -y python3 python3-pip

python3 -m pip install --break-system-packages flask pytest
python3 -m pytest
```

---

### ✔️ Outcome

* Python installed dynamically
* Dependencies installed
* Tests executed successfully
* Build marked as SUCCESS

---

## 🔄 CI/CD Workflow

```
Developer → Git Push → GitHub Actions (CI)
                         ↓
                   Automated Testing
                         ↓
                    Docker Build
                         ↓
                   Jenkins Build
                         ↓
                   Final Validation
```

---

## 🎯 Key Achievements

* Implemented complete CI/CD pipeline
* Automated testing and validation
* Ensured consistent environment using Docker
* Integrated GitHub Actions and Jenkins

---

## 📌 Conclusion

This project successfully demonstrates modern DevOps practices including:

* Continuous Integration
* Automated Testing
* Containerization
* Build Automation

The pipeline ensures reliable, scalable, and efficient software delivery.

