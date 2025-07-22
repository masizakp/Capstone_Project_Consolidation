# My Django Project

This repository contains a Django web application.

## Getting Started

These instructions will help you set up and run the project locally using a Python virtual environment or Docker.

---

## Prerequisites

- Python 3.8+
- pip (Python package installer)
- Docker (optional, for containerized deployment)

---

## Clone the Repository

git clone https://github.com/masizakp/Capstone_Project_Consolidation.git
cd Capstone_Project_Consolidation

 ## 1. Create a virtual environment:
    python -m venv venv

 ## 2. Activate the virtual environment:

    Windows (Command Prompt):
    venv\Scripts\activate

    Windows (PowerShell):
    .\venv\Scripts\Activate.ps1

    macOS/Linux:
    source venv/bin/activate

 ## 3. Run the application:
    python manage.py runserver

## Run with Docker:
## 1. Clone the repository:
    git clone https://github.com/masizakp/Capstone_Project_Consolidation.git
    cd Capstone_Project_Consolidation

 ## 2. Build the Docker image:
    docker build -t Capstone_Project_Consolidation .
## 3. Run the Docker container:
    docker run -p 8000:8000 Capstone_Project_Consolidation
    