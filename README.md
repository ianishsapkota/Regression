# Multiple Linear Regression on 50 Startups Dataset

This project demonstrates how to apply **Multiple Linear Regression** on the popular **50_Startups** dataset to predict company profits based on R&D Spend, Administration, Marketing Spend, and State.

## 📌 Project Overview

The goal of this project is to:

* Preprocess the dataset (including categorical encoding)
* Split data into training and test sets
* Train a Linear Regression model
* Predict profits for the test set
* Compare predicted results with actual values

This project is ideal for beginners learning **Machine Learning**, **Data Preprocessing**, and **Regression Models**.

---

## 🧠 Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib (optional for visualization)
* Scikit-learn

---

## 📂 Dataset

The dataset used in this project is:

```
50_Startups.csv
```

It contains the following columns:

* R&D Spend
* Administration
* Marketing Spend
* State (Categorical)
* Profit (Target)

---

## 🚀 How It Works

### 1. **Import Libraries**

Essential libraries such as NumPy, Pandas, Matplotlib, and scikit-learn.

### 2. **Load Dataset**

```python
dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
```

### 3. **Encode Categorical Data**

```python
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))
```

### 4. **Split Dataset**

```python
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
```

### 5. **Train the Model**

```python
mlr = LinearRegression()
mlr.fit(x_train, y_train)
```

### 6. **Make Predictions**

```python
y_pred = mlr.predict(x_test)
```

### 7. **View Results**

```python
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), axis=1))
```

This displays predicted vs actual profit side by side.

---

## 📊 Example Output

```
[[103015.2 103282.38]
 [132582.3 144259.4 ]
 [132447.7 146121.95]
 ...]
```

---

Happy Coding! 🚀
