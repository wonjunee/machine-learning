import numpy as np
from sklearn import svm

X = [[0,0],[1,1]]
y = [0,1]
clf = svm.SVC()
clf.fit(X,y)

# predict
pred = clf.predict([[0.1,0.1]])
print pred

# Calculate the accuracy
from sklearn.metrics import accuracy_score
labels_test = [[1]]
acc = accuracy_score(pred, labels_test)
print acc