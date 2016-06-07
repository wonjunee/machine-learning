#!/usr/bin/python
import numpy as np

"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


### using train test split validation
from sklearn import cross_validation

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
	features, labels, test_size=0.3, random_state=42)

### Import decision tree library
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

print "How many POIs in the test set? :", np.sum(pred)
print "How many people in the test set? :", np.size(pred)

### Creating a test set with 0's
pred_zero = pred * 0

### Accuracy
from sklearn.metrics import accuracy_score

acc = accuracy_score(pred,labels_test)
print "accuracy of the test set:", acc
acc = accuracy_score(pred_zero,labels_test)
print "accuracy of the zero test set:", acc

### Finding the true positive
true_positive_count = 0
for i in range(len(labels_test)):
	if labels_test[i] == pred[i] and pred[i] == 1:
		true_positive_count+=1
print "true positive count:", true_positive_count

### Using precision score
from sklearn.metrics import precision_score

precision_acc = precision_score(pred,labels_test)
print "precision score:", precision_acc

### Create a function for finding true negative
def true_negative(prediction, labels):
	count = 0 
	for i in range(len(predictions)):
		if predictions[i] == 0 and labels[i] == 0:
			count += 1
	return count

def false_positive(prediction, labels):
	count = 0 
	for i in range(len(predictions)):
		if predictions[i] == 1 and labels[i] == 0:
			count += 1
	return count

def false_negative(prediction, labels):
	count = 0 
	for i in range(len(predictions)):
		if predictions[i] == 0 and labels[i] == 1:
			count += 1
	return count

def true_positive(prediction, labels):
	count = 0 
	for i in range(len(predictions)):
		if predictions[i] == 1 and labels[i] == 1:
			count += 1
	return count
### Finding true negative with an example
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

print "true_positive:", true_positive(predictions, true_labels)
print "true_negative:", true_negative(predictions, true_labels)
print "false_positive:", false_positive(predictions, true_labels)
print "false_negative:", false_negative(predictions, true_labels)