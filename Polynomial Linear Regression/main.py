import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('data.csv')
x = df.iloc[:,1].values.reshape(-1, 1) 
y = df.iloc[:,-1].values

# Train linear regression model
lr = LinearRegression()
lr.fit(x, y)

# Visualize linear regression results
plt.scatter(x, y, color='red')
plt.plot(x, lr.predict(x), color='blue') 
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.show()