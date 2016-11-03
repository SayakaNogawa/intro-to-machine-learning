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

i = 0
for user in enron_data:
    if enron_data[user]["poi"] == True:
        i = i + 1
print i

fo = open('../final_project/poi_names.txt','r')
fr = fo.readlines()
print len(fr[2:])

enron_data['SKILLING JEFFREY K'].keys()
enron_data.keys()
james = enron_data['PRENTICE JAMES']['total_stock_value']
print james

colwell = enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print colwell

skilling = enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print skilling

sorted(enron_data.keys())
K = enron_data['SKILLING JEFFREY K']['total_payments']
L = enron_data['LAY KENNETH L']['total_payments']
S = enron_data['FASTOW ANDREW S']['total_payments']
print K , L , S

non = enron_data['FASTOW ANDREW S']['deferral_payments']
print non

count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary += 1
    if enron_data[key]['email_address'] != 'NaN':
        count_email +=1
print count_salary
print count_email


"""optional"""

count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp += 1

print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())


count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        count_NaN_tp+=1

print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())
