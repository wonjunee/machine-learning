#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### it's all yours from here forward!

### Finding the shape of the data
h, w = data.shape

### set up the train data
features_train = data[:,1].reshape(h, 1)
labels_train = data[:,0].reshape(h,1)

### Import decision tree library
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)
pred = clf.predict(features)

### Accuracy
from sklearn.metrics import accuracy_score

acc = accuracy_score(pred,labels)
print "accuracy:", acc