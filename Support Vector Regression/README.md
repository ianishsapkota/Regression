# Salary Prediction using Support Vector Regression (SVR)

A machine learning project that predicts salaries based on position levels using Support Vector Regression with RBF kernel.

## Overview

This project demonstrates the application of SVR to predict employee salaries across different organizational levels. The model uses feature scaling and the Radial Basis Function (RBF) kernel to capture non-linear relationships between position levels and compensation.

## Dataset

The dataset contains 15 entries representing typical organizational hierarchy:

- **Features**: Position Level (1-15)
- **Target**: Salary ($25,000 - $500,000)
- **Range**: From Intern to Senior Vice President

Sample data:
| Position | Level | Salary |
|----------|-------|---------|
| Intern | 1 | $25,000 |
| Junior Analyst | 2 | $35,000 |
| ... | ... | ... |
| Senior Vice President | 15 | $500,000 |

## Requirements

```bash
numpy
pandas
matplotlib
scikit-learn
```

Install dependencies:
```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage

1. Ensure `data.csv` is in the same directory as the script
2. Run the Python script:

```bash
python salary_prediction.py
```

## Model Details

- **Algorithm**: Support Vector Regression (SVR)
- **Kernel**: Radial Basis Function (RBF)
- **Preprocessing**: StandardScaler for both features and target
- **Prediction Example**: Level 6.5 position salary

### Key Steps

1. **Data Loading**: CSV file with position levels and salaries
2. **Feature Scaling**: Standardization applied to both X and y
3. **Model Training**: SVR with RBF kernel fitted on scaled data
4. **Prediction**: Inverse transformation for real-world salary values
5. **Visualization**: Scatter plot of actual data with SVR curve

## Visualization

The script generates a plot showing:
- Red scatter points: Actual salary data
- Blue curve: SVR prediction line
- Demonstrates the model's ability to capture non-linear salary progression

## Model Performance

SVR with RBF kernel is particularly effective for this dataset because:
- Captures non-linear salary growth patterns
- Handles the exponential increase in compensation at higher levels
- Provides smooth predictions across the entire range