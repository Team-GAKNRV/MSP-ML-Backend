# MSP-ML-Backend
Backend for our ml model for the MSP project.

## Project Structure
This is the basic project structure:
```
MSP-ML-Backend
├── main.py
├── api
│   ├── v1
│   │   ├── api.py
│   │   └── endpoints.py
├── core
│   ├── labels
│   │   └── model_x_labels.pkl
│   ├── models
│   │   └── model_x.pt
│   ├── scripts
│   │   └── classification.py
│   └── settings.py
└── docs
    └── images
        └── model_x-metrics.jpg
```

## Basic Setup
1. You need to have `Python 3.10` or greater.
1. Setup a virtual environment with `python -m venv .venv`
1. Activate the virtual environment with `source .venv/Scripts/activate` (the path and file may change, depending on your operating system)
1. Install all dependencies with `pip install -r requirements.txt`

> Note: On Linux you may have to replace `python` with `python3`.

## Basic Usage
Run the project with `python main.py`

> Note: On Linux you may have to replace `python` with `python3`.
