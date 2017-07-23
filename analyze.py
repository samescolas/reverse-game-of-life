#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection, preprocessing
import xgboost as xgb

num_examples = 10

pd.options.mode.chained_assignment = None

train_df = pd.read_csv('train.csv', nrows=num_examples)

stop = ['stop.' + str(x) for x in xrange(1,401)]
start = ['start.' + str(x) for x in xrange(1,401)]

data = train_df[stop].stack()
outcomes = train_df[start].stack()
deltas = train_df['delta'].values

processed_data = pd.DataFrame

for board in xrange(num_examples):
	df = pd.DataFrame([
		[board]*400,
		[deltas[board]]*400,
		range(1,401),
		list(data[board].values.transpose()),
		list(outcomes[board].values.transpose()),
		[sum(data[board])]*400
	])

	if processed_data.empty:
		processed_data = df.transpose()
	else:
		processed_data = pd.concat([processed_data, df.transpose()])

print processed_data.head(800)
print processed_data.tail(800)
