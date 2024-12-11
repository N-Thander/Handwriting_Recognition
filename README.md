# Handwriting_Recognition

### Project Structure

```
Project/
├── backend/                     # Backend folder
│   ├── app/                     # FastAPI app
│   │   ├── __init__.py
│   │   ├── main.py              # Entry point for FastAPI app
│   │   ├── api/                 # API routes
│   │   │   ├── __init__.py
│   │   │   ├── routes.py        # Define API endpoints
│   │   ├── core/                # Core logic and configuration
│   │   │   ├── __init__.py
│   │   │   ├── config.py        # App configurations
│   │   │   ├── model.py         # ML model loading and prediction logic
│   │   ├── utils/               # Utility functions
│   │   │   ├── __init__.py
│   │   │   ├── preprocessing.py # Preprocessing helper for the model
│   │   │   ├── postprocessing.py # Postprocessing helper for predictions
│   │   ├── static/              # Static assets served via backend
│   │       ├── uploaded_files/  # Stores uploaded files temporarily
│   ├── models/                  # Machine learning model files
│   │   ├── handwriting_model.h5 # ML model for handwriting recognition
│   ├── tests/                   # Test cases for the backend
│       ├── test_api.py          # API test cases
│       ├── test_model.py        # Model-specific test cases
├── frontend/                    # Frontend folder
│   ├── index.html               # Main HTML file
│   ├── styles/                  # CSS files
│   │   ├── style.css            # Stylesheet
│   ├── scripts/                 # JavaScript files
│       ├── main.js              # Main JS for interactions
│       ├── api.js               # Functions for calling the backend API
├── .env                         # Environment variables
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
```

