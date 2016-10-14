#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
#from sklearn.svm import SVC
from sklearn.svm import SVC

clf_rbf = SVC(kernel='rbf',C=10000)

clf_rbf.fit(features_train,labels_train)

t0 = time()
clf_rbf.fit(features_train,labels_train)
print "learining time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf_rbf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print(acc)

print(sum(pred))

#########################################################
