# SentinelRAT

SentinelRAT is a Python-based demonstration of an authorized endpoint monitoring and administration platform.

## Features

- Authenticated API
- Device enrollment
- Device inventory
- Basic system telemetry
- Allowlisted action registry
- Security audit logging
- Streamlit dashboard
- Command-line interface
- Automated tests

## Requirements

- Python 3.11 or later
- Visual Studio Code or another Python editor

## Installation

Create and activate a virtual environment.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file based on `.env.example` and configure a secure API key.

## Start the API

```bash
python -m uvicorn server.main:app --host 127.0.0.1 --port 8000 --reload
```

API documentation:

http://127.0.0.1:8000/docs

## Start the dashboard

In another terminal:

```bash
python -m streamlit run dashboard/app.py
```

## Start the demonstration client

```bash
python -m agent.main
```

## Run tests

```bash
python -m pytest -v
```

## Security

Use this project only on systems you own or are explicitly authorized to administer.

The current implementation is intended for local development and education. It is not a production-ready remote administration or endpoint detection platform.

Before deployment, implement HTTPS, individual device credentials, role-based access control, secure enrollment, database migrations, and hardened audit logging.