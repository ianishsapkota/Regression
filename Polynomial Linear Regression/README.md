<<<<<<< HEAD
# Salary Prediction Using Regression Models

This project predicts salaries based on job position levels using Linear Regression and Polynomial Regression models.

## Dataset

The dataset contains salary information for 15 different positions:

- **Columns**: Position, Level, Salary
- **Range**: Intern (Level 1) to Senior Vice President (Level 15)
- **Salary Range**: $25,000 - $500,000

## Requirements

```bash
pip install numpy pandas matplotlib scikit-learn
```


## How It Works

### 1. Data Loading
```python
df = pd.read_csv('data.csv')
x = df.iloc[:,1].values.reshape(-1, 1)  # Level column
y = df.iloc[:,-1].values                 # Salary column
```

### 2. Linear Regression
Fits a simple linear model to predict salary based on level.

### 3. Polynomial Regression
Fits a 4th-degree polynomial model for better accuracy with non-linear relationships.

## Usage

Run the script:
```bash
python main.py
```

### Making Predictions

```python
# Predict salary for level 6.5 using Linear Regression
lr.predict([[6.5]])

# Predict salary for level 6.5 using Polynomial Regression
lr_2.predict(pr.fit_transform([[6.5]]))
```

## Visualizations

The script generates two plots:

1. **Linear Regression**: Shows linear fit to the data
2. **Polynomial Regression**: Shows 4th-degree polynomial fit (more accurate for this dataset)

## Results

- **Linear Regression**: Good for understanding general trend
- **Polynomial Regression**: Better captures the non-linear salary growth pattern
- Polynomial model provides more accurate predictions for intermediate levels

## Model Performance

=======
# Salary Prediction Using Regression Models

This project predicts salaries based on job position levels using Linear Regression and Polynomial Regression models.

## Dataset

The dataset contains salary information for 15 different positions:

- **Columns**: Position, Level, Salary
- **Range**: Intern (Level 1) to Senior Vice President (Level 15)
- **Salary Range**: $25,000 - $500,000

## Requirements

```bash
pip install numpy pandas matplotlib scikit-learn
```


## How It Works

### 1. Data Loading
```python
df = pd.read_csv('data.csv')
x = df.iloc[:,1].values.reshape(-1, 1)  # Level column
y = df.iloc[:,-1].values                 # Salary column
```

### 2. Linear Regression
Fits a simple linear model to predict salary based on level.

### 3. Polynomial Regression
Fits a 4th-degree polynomial model for better accuracy with non-linear relationships.

## Usage

Run the script:
```bash
python main.py
```

### Making Predictions

```python
# Predict salary for level 6.5 using Linear Regression
lr.predict([[6.5]])

# Predict salary for level 6.5 using Polynomial Regression
lr_2.predict(pr.fit_transform([[6.5]]))
```

## Visualizations

The script generates two plots:

1. **Linear Regression**: Shows linear fit to the data
2. **Polynomial Regression**: Shows 4th-degree polynomial fit (more accurate for this dataset)

## Results

- **Linear Regression**: Good for understanding general trend
- **Polynomial Regression**: Better captures the non-linear salary growth pattern
- Polynomial model provides more accurate predictions for intermediate levels

## Model Performance

>>>>>>> e64e57f0b7ab75083bc3ab13fd027659454733a4
The polynomial model (degree=4) better captures the exponential growth in salaries at higher positions compared to the linear model.