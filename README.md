# Car Price Prediction Project

## Overview
This project predicts the selling price of used cars based on various features such as car age, mileage, fuel type, transmission, and ownership details. It uses Machine Learning to learn patterns from historical car data and estimate a fair market price.

## Steps
1. Data cleaning and preprocessing
2. Handling missing values
3. Encoding categorical features
4. Feature scaling
5. Model training using Random Forest
6. Model evaluation
7. Prediction on new/unseen data

## Model Used
- Random Forest Regressor
- Handles non-linear relationships well
- Robust to outliers
- Performs well on tabular data

## Project Structure
```
flask3/
│
├── templates/
│   └── index.html
│
├── app.py                 # Flask application
├── train_reg.py           # Training script for regression model
├── classifier.py          # Classifier script
├── car_prediction_data.csv # Dataset used for training
├── requirements.txt       # Dependencies
├── Dockerfile             # Docker configuration
├── Procfile               # Deployment configuration
├── README.md              # Project documentation
```

## How to Run

### 1. Clone the repository
```bash
git clone <repository-url>
cd flask3
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

## Results
The model provides reliable car price predictions and performs well on unseen data after tuning.

## Future Improvements
- Integrate additional machine learning models for comparison
- Add real-time data fetching capabilities
- Implement advanced hyperparameter tuning techniques
- Enhance deployment scalability for high traffic

## Author
Rizin Ahammed N

## 🔗 Live Demo
[🚀 Click here to try the app](https://car-prediction1.onrender.com/)
