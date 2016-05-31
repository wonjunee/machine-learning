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
		
	
