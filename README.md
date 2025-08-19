# FastAPI CI Project

This is a simple FastAPI application designed to demonstrate how to build and test API routes using `pytest`, with automated CI integration via GitHub Actions.

## Features

- **Three API routes**:
  - `GET /health` – Basic health check
  - `GET /hello/{name}` – Personalized greeting
  - `POST /items` – Create a new item with name and price

- **Nine automated tests** using `pytest`, covering all routes and edge cases

- **Continuous Integration** with GitHub Actions to automatically run tests on every push or pull request

## Running the App Locally

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload

## Screenshot 

<img width="1907" height="830" alt="image" src="https://github.com/user-attachments/assets/718bf2b9-7a31-44f7-bb85-38eb8244a522" />
