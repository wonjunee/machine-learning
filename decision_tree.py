from sklearn import tree
X = [[0,0], [1,1]]
Y = [0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

pred = clf.predict([[2,2]])

# Accuracy
from sklearn.metrics import accuracy_score

acc = accuracy_score(pred,[1])
print "accuracy:", acc