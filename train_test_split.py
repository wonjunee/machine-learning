import numpy as np
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
print "iris.data.shape:", iris.data.shape
print "iris.target.shape:", iris.target.shape

from sklearn import cross_validation

X_train, X_test, y_train, y_test = cross_validation.train_test_split(
	iris.data, iris.target, test_size=0.4, random_state=0)

print "X_train.shape:", X_train.shape
print "y_train.shape:", y_train.shape

print "X_test.shape:", X_test.shape
print "X_test.shape:", y_test.shape

### C=1 -> Penalty parameter C of the error term
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print "\nScore:", clf.score(X_test, y_test)