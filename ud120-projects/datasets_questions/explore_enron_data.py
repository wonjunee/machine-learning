#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0
for k,v  in enron_data.iteritems():
	if v['poi']:
		count+=1

print count


# Finding the person who took the largest money
import pprint 
poi = ["LAY", "SKILLING", "FASTOW"]

for k,v  in enron_data.iteritems():
	for key in k.split(" "):
		if key in poi:
			print k
			pprint.pprint(v["total_payments"])


# How many folks in this dataset have a quantified salary? What about a known email address?
email = 0
salary = 0
for k, v in enron_data.iteritems():
	if v["email_address"] != "NaN":
		email+=1
	if v["salary"] != "NaN":
		salary+=1


print email
print salary

## How many people in the E+F dataset (as it currently exists) have 
## NaN for their total payments? What percentage of people in the dataset as a whole is this?

count = 0
NaN = 0
for k, v in enron_data.iteritems():
	count += 1
	if v["total_payments"] == "NaN":
		NaN += 1

print NaN*100/count

# How many POIs in the E+F dataset have NaN for their total payments? 
# What percentage of POIs as a whole is this?

count = 0
NaN = 0
for k, v in enron_data.iteritems():
	count += 1
	if v["total_payments"] == "NaN":
		NaN += 1

print count
print NaN

# What is the new number of POI’s in the dataset? 
# What percentage of them have NaN for their total stock value?

