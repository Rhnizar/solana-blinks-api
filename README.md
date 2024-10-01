# Solana Actions API

## Overview

This project is a structured Django REST API designed to interact with Solana blockchain actions. It provides a clean and organized codebase, integrated with Docker for easy development and deployment.

## Project Structure

solana-api-server/
├── backend/                 # Contains Django backend
│   ├── solana_actions/      # Django app for Solana actions
│   ├── manage.py            # Django management script
│   └── requirements.txt     # Python dependencies for the backend
│
├── frontend/                # Contains frontend application
│   └── src/                 # Source files for the frontend
│
├── .env                     # Environment variables
├── .gitignore               # Files to ignore in git
├── docker-compose.yml       # Docker Compose configuration
├── README.md                # Project documentation



## Technologies Used

- **Django**: Web framework for building the REST API.
- **Django REST Framework**: Toolkit for building Web APIs in Django.
- **Solana**: Blockchain platform for integrating Solana actions.
- **Docker**: Containerization tool for developing and running applications in isolated environments.
- **Nginx**: Web server used to serve the frontend application efficiently

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:Rhnizar/solana-blinks-api.git
   cd solana-api-server

2. Run Command:
    ```bash
    docker-compose up --build