### Min max scalar example script
import numpy as np

X_train = np.array([[1., -1., 2.],
					[2.,  0., 0.],
					[0.,  1.,-1.]])

from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(X_train)
print X_train_minmax

### Second example
weights = np.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print rescaled_weight