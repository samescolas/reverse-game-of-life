#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVR
from sklearn.feature_selection import RFE
import xgboost as xgb
from data_processing import get_neighbors,get_size

num_examples = 1000

pd.options.mode.chained_assignment = None

train_df = pd.read_csv('resources/train.csv', nrows=num_examples)

stop = ['stop.' + str(x) for x in xrange(1,401)]
start = ['start.' + str(x) for x in xrange(1,401)]

data = train_df[stop].stack()
outcomes = train_df[start].stack()
deltas = train_df['delta'].values
types = ([1]+[2]*18+[1]) + ([2]+[3]*18+[2])*18 + ([1]+[2]*18+[1])

cols = ['board', 'delta', 'position', 'size', 'type', 'alive', 'neighbors', 'population', 'outcome']

processed_data = pd.DataFrame

for board in xrange(num_examples):
	print str(100 * (float(board)/num_examples)) + '%'
	df = [
		[board]*400,
		[deltas[board]]*400,
		range(1,401),
		[get_size(x, data[board].values) for x in xrange(400)],
		[types[x] for x in xrange(400)],
		list(data[board].values.transpose()),
                [get_neighbors(x, data[board].values) for x in xrange(400)],
		[sum(data[board])]*400,
		list(outcomes[board].values.transpose())
	]
	df = [list(l) for l in zip(*df)]
	df = pd.DataFrame(df, columns=cols)
	if processed_data.empty:
		processed_data = df
	else:
		processed_data = pd.concat([processed_data, df], ignore_index=True)

X = processed_data.drop('outcome', axis=1)
y = processed_data['outcome']

#Xtrain,Xtest,ytrain,ytest = train_test_split(X, y, random_state=1)

estimator = SVR(kernel="linear")
selector = RFE(estimator, 5, step=1)
selector = selector.fit(X,y)
print selector.support_
print selector.ranking_
print cols[0:-1]

#model = LogisticRegression()
#rfe = RFE(model, 3)
#rfe.fit(X, y)

#print rfe.support_
#print rfe.ranking_

#model = GaussianNB()
#model.fit(Xtrain, ytrain)
#y_model = model.predict(Xtest)

#print str(accuracy_score(ytest, y_model))
