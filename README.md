# MSP-ML-Backend
Backend for our ml model for the MSP project.

## Project Structure
This is the basic project structure:
```
MSP-ML-Backend
├── __init__.py
├── main.py
├── core
│   ├── models
│   │   ├── database.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── schema.py
│   └── settings.py
└── v1
    ├── api.py
    ├── endpoints
    │   ├── endpoint.py
    │   └── __init__.py
    └── __init__.py 
```

## Basic Usage
Run the project with: `uvicorn main:app --reload`
