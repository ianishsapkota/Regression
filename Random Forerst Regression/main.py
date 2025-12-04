import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

dataset = pd.read_csv('data.csv', delimiter=',')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)

print("Predictions vs Actual:")
comparison = np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), axis=1)
print(comparison)

print("\nR² Score:", r2_score(y_test, y_pred))

plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, color='red', label='Actual Prices')
plt.scatter(range(len(y_pred)), y_pred, color='blue', label='Predicted Prices')
plt.title('Random Forest Regression: Actual vs Predicted House Prices')
plt.xlabel('Test Sample Index')
plt.ylabel('House Price')
plt.legend()
plt.tight_layout()
plt.show()