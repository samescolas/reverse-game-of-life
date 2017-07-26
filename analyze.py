#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVR
from sklearn.feature_selection import RFE
import xgboost as xgb
from data_processing import process_data

processed_data = process_data('resources/train.csv', 1000)

X = processed_data.drop('outcome', axis=1)
y = processed_data['outcome']

#Xtrain,Xtest,ytrain,ytest = train_test_split(X, y, random_state=1)

print processed_data.head(100)
print processed_data.tail(42)

#model = LogisticRegression()
#rfe = RFE(model, 3)
#rfe.fit(X, y)

#print rfe.support_
#print rfe.ranking_

#model = GaussianNB()
#model.fit(Xtrain, ytrain)
#y_model = model.predict(Xtest)

#print str(accuracy_score(ytest, y_model))
