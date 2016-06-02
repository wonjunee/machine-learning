#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

data_dict.pop("TOTAL",0)

data = featureFormat(data_dict, features)

### your code below

## Checking Outliers - 1
for k,v in data_dict.iteritems():
	if v["salary"] > 2.5e7 and v["salary"] != "NaN":
		print k
		print v["salary"]

## Checking Outliers - 2
for k,v in data_dict.iteritems():
	if v["salary"] > 1000000 and v["bonus"] > 5000000 and v["salary"] != "NaN":
		print k

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()