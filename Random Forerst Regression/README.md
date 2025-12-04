# Random Forest Regression - House Price Prediction

## Overview
This project implements a Random Forest Regression model to predict house prices based on various property features. Random Forest is an ensemble learning method that uses multiple decision trees to provide more accurate and stable predictions.

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
- **Algorithm**: Random Forest Regressor
- **Number of Trees**: 100 (n_estimators=100)
- **Train-Test Split**: 80% training, 20% testing
- **Random State**: 0 (for reproducibility)

## Output
The script provides:
1. **Predictions vs Actual values**: Console output showing predicted and actual house prices
2. **R² Score**: Model performance metric (closer to 1 is better)
3. **Visualization**: Scatter plot comparing actual prices (red) vs predicted prices (blue)

## Model Performance
The R² score indicates how well the model predicts house prices. Random Forest typically achieves higher accuracy than single Decision Trees due to:
- **Ensemble Learning**: Combines predictions from multiple trees
- **Reduced Overfitting**: Averaging reduces variance
- **Better Generalization**: More robust to noise in data

## Files
- `main.py`: Main script with Random Forest Regression implementation
- `data.csv`: Dataset containing house features and prices
- `README.md`: This file

## How Random Forest Regression Works
Random Forest is an ensemble method that:
1. Creates multiple decision trees using random subsets of data
2. Each tree makes its own prediction
3. Final prediction is the average of all tree predictions
4. This approach reduces overfitting and improves accuracy

### Advantages over Single Decision Tree
- **Higher Accuracy**: Multiple trees provide better predictions
- **Less Overfitting**: Averaging reduces model variance
- **Handles Non-linearity**: Can capture complex relationships
- **Feature Importance**: Shows which features matter most