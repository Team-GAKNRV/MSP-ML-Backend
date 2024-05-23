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

## Basic Usage
Run the project with: `uvicorn main:app --reload`
