# Profile API

A simple FastAPI service that returns user profile information along with a random cat fact fetched from an external API (https://catfact.ninja/fact).

## Prerequisites

- Python 3.8+
- pip

## Setup Instructions

1.  **Clone the Repository**
    If you haven't already, clone the repository to your local machine.
    ```bash
    git clone profile-api
    cd profile-api
    ```

2.  **Create and Activate Virtual Environment (Optional)**
    A virtual environment makes it easier to manage project-specific dependencies.

    ```bash
    python3 -m venv venv
    ```

    To activate the environment on Linux/MacOS use:
    ```bash
    source venv/bin/activate
    ```

    On Windows, use:
    ```bash
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install all required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

With the dependencies installed, you can run the application using:

```bash
fastapi dev main.py
```

The API will be running and accessible at `http://127.0.0.1:8000`.

## Running Tests

To run the automated tests for this project, use `pytest`. The `-v` flag provides a more verbose output.

```bash
pytest -v
```


## API Documentation
You can access the documentation on http://127.0.0.1:8000/docs.

