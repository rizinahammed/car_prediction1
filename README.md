# Car Price Predictor

## About

This is a Flask-based web application that predicts the selling price of a car based on various features such as showroom price, kilometers driven, number of owners, age of the car, fuel type, seller type, and transmission type. The prediction is made using a machine learning model (VotingRegressor combining Linear Regression and Random Forest) trained on historical car data.

## Video/GIF Demo

![Car Price Predictor Demo](demo.gif)

*Replace with actual demo video or GIF showing the app in action.*

## How to Setup

### Prerequisites
- Python 3.12 or higher
- pip

### Local Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flask3
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Train the model (if model.pkl doesn't exist):
   ```bash
   python train_reg.py
   ```

5. Run the Flask application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000`

## Deployed App

### Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t car-price-predictor .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 car-price-predictor
   ```

### Heroku Deployment
1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create a new app: `heroku create your-app-name`
4. Push to Heroku: `git push heroku main`
5. Open the app: `heroku open`

*Deployed app link: [Insert deployed app URL here]*