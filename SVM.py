import numpy as np
from sklearn import svm

X = [[0,0],[1,1]]
y = [0,1]
clf = svm.SVC()
clf.fit(X,y)

print clf.predict([[0.1,0.1]])
