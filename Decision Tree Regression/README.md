# Decision Tree Regression - House Price Prediction

## Overview
This project implements a Decision Tree Regression model to predict house prices based on various property features such as size, number of bedrooms, location, and other factors.

## Dataset
The dataset (`data.csv`) contains 59 house records with the following features:

### Features (Input Variables)
- **Size_sqft**: Size of the house in square feet
- **Bedrooms**: Number of bedrooms
- **Bathrooms**: Number of bathrooms
- **Age**: Age of the house in years
- **DistanceFromCity_km**: Distance from city center in kilometers
- **CrimeRate**: Crime rate in the area
- **SchoolRating**: Rating of nearby schools (scale 1-10)

### Target Variable
- **HousePrice**: Price of the house in dollars

## Requirements
```
numpy
matplotlib
pandas
scikit-learn
```

Install dependencies:
```bash
pip install numpy matplotlib pandas scikit-learn
```

## Usage
1. Ensure `data.csv` is in the same directory as the Python script
2. Run the script:
```bash
python main.py
```

## Model Details
- **Algorithm**: Decision Tree Regressor
- **Train-Test Split**: 80% training, 20% testing
- **Random State**: 0 (for reproducibility)

## Output
The script provides:
1. **Predictions vs Actual values**: Console output showing predicted and actual house prices
2. **R² Score**: Model performance metric (closer to 1 is better)
3. **Visualization**: Scatter plot comparing actual prices (red) vs predicted prices (blue)

## Model Performance
The R² score indicates how well the model predicts house prices. A score close to 1.0 means excellent predictions, while a score closer to 0 indicates poor performance.

## Files
- `main.py`: Main script with Decision Tree Regression implementation
- `data.csv`: Dataset containing house features and prices
- `README.md`: This file

## How Decision Tree Regression Works
Decision Tree Regression creates a tree-like model of decisions based on the features. It splits the data into branches based on feature values to make predictions. Unlike linear models, it can capture non-linear relationships in the data.