# Fake News Detector

A React web application that uses a Python machine learning model to detect fake news. The backend Python files are deployed in the `res` folder.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Backend Details](#backend-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Fake News Detector is a web application built with React for the frontend and a Python machine learning model for the backend. It allows users to input news articles or headlines and receive a classification on whether the news is real or fake.

## Features

- **User-friendly Interface:** Easy-to-use interface for checking the authenticity of news articles.
- **Real-time Analysis:** Quickly processes input to determine the likelihood of news being fake.
- **Machine Learning:** Utilizes a trained machine learning model for accurate predictions.

## Installation

### Prerequisites

- Node.js
- Python 3.x
- pip (Python package installer)

### Frontend Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/LavKalsi/FakeNewsDetector.git
    cd FakeNewsDetector
    ```

2. Navigate to the `frontend` directory and install dependencies:
    ```sh
    cd frontend
    npm install
    ```

3. Start the React application:
    ```sh
    npm start
    ```

### Backend Setup

1. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the required Python packages:
    ```sh
    pip install -r res/requirements.txt
    ```

3. Run the backend server:
    ```sh
    python res/app.py
    ```

## Usage

1. Ensure both the frontend and backend servers are running.
2. Open your browser and navigate to `http://localhost:3000`.
3. Enter the news article or headline you want to verify.
4. Click the "Check" button to receive the classification result.

## How It Works

The Fake News Detector web app allows users to easily check the authenticity of news articles. Here's how you can use it:

1. **Input News:** Users can input a news article or headline into the provided text box on the web app.
2. **Submit for Analysis:** After entering the news, users click the "Check" button to submit the text for analysis.
3. **Backend Processing:** The frontend sends the news text to the backend Python server, where the machine learning model processes it.
4. **Receive Results:** The backend returns the analysis result (real or fake) to the frontend, which is then displayed to the user.

## Backend Details

The backend is a Python Flask application that serves a machine learning model trained to classify news as real or fake. The backend files, including the model and Flask app, are located in the `res` folder.

### Files in `res` Folder

- `app.py`: The Flask application that handles HTTP requests from the frontend.
- `model.pkl`: The trained machine learning model.
- `requirements.txt`: The dependencies required for the Python backend.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

LavKalsi - [GitHub](https://github.com/LavKalsi)

Feel free to contact me if you have any questions or suggestions!
