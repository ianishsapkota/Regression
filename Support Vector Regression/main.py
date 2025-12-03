import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

df = pd.read_csv('data.csv')
x = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values

#feature scaling
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y.reshape(-1, 1))

regressor = SVR(kernel = 'rbf')
regressor.fit(x, y.ravel())

prediction = sc_y.inverse_transform(regressor.predict(sc_x.transform([[6.5]])).reshape(-1,1))

plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_x.inverse_transform(x), sc_y.inverse_transform(regressor.predict(x).reshape(-1,1)), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()