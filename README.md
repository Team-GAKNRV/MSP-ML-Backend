# MSP-ML-Backend
Backend for our ml model for the MSP project.

## Project Structure
This is the basic project structure:
```
MSP-ML-Backend
├── .env
├── main.py
├── requirements.txt
├── api
│   ├── v1
│   │   ├── api.py
│   │   └── endpoints.py
├── core
│   ├── labels
│   │   └── model_x_labels.pkl
│   ├── models
│   │   └── model_x.pt
│   └── scripts
│       └── classification.py
├── docs
│   └── images
│       └── model_x-metrics.jpg
└── temp
    └── temp_image.jpg
```

- `.env`: Holds necessary variables for the project to work (needs to be created by the user)
- `main.py`: Entry point of the application
- `requirements.txt`: List of all dependencies for the project
- `api`: Holds all api versions and endpoints of the project
- `core`
  - `labels`: Pickled files of the labels
  - `models`: Models for each label
  - `scripts`: Scripts for classification and utils used in the api
- `docs`: Documentation stuff
- `temp`: Temporary storage for e.g. input images received via an api request

## Basic Setup
1. You need to have `Python 3.10` or greater.
1. Set up a virtual environment with `python -m venv .venv`
1. Activate the virtual environment with `source .venv/Scripts/activate` (the path and file may change, depending on your operating system)
1. Install all dependencies with `pip install -r requirements.txt`

## Basic Usage
Run the project with `python main.py`
