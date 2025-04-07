# Sentiment Analysis Application

A web application that analyzes the sentiment of text using FastAPI and a modern frontend interface.

## Features

- Modern, responsive frontend interface
- Real-time sentiment analysis
- RESTful API backend
- CORS support for frontend-backend communication
- Static file serving

## Project Structure

```
.
├── frontend/           # Frontend files
│   ├── index.html     # Main HTML file
│   └── styles.css     # CSS styles
├── app.py             # FastAPI backend
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

## API Endpoints

- `GET /`: Serves the frontend interface
- `POST /analyze`: Analyzes text sentiment
  - Request body: `{"text": "your text here"}`
  - Response: `{"text": "input text", "sentiment": "POSITIVE/NEGATIVE", "score": 0.95}`

## Development

The application is built with:
- FastAPI for the backend
- HTML/CSS for the frontend
- Transformers for sentiment analysis

## Contributing

1. Create a new branch for your feature:
```bash
git checkout -b feature-name
```

2. Make your changes and commit them:
```bash
git add .
git commit -m "Description of changes"
```

3. Push to your branch:
```bash
git push origin feature-name
```

4. Create a pull request on GitHub

## License

This project is open source and available under the MIT License.