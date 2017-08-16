#!/usr/bin/python
#precogtask

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import pickle
import matplotlib.pyplot as plt
import time

headers = ['channelAge', 'videoAge', 'viewCount', 'commentCount', 'favoriteCount','channel_commentCount', 'channel_subsriberCount', 'channel_ViewCount', 'channelViewCount/channeVideoCount', 'viewCount/videoAge', 'subscriberCount/channelVideoCount', 'channel_subsriberCount/channelAge']

df = pd.read_csv("trainFood.csv")
 
X = df[headers]
Y = df.likeCount

# parameters
n_estimators = 200
max_depth = 25
min_samples_split=15
min_samples_leaf=2


# Random forest classifier
clf = RandomForestRegressor(n_estimators = n_estimators, max_depth = max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
X = np.concatenate((X,X),axis=0)
Y = np.concatenate((Y,Y),axis=0)

clf.fit(X,Y)

file_name = "RandomForestRegressor"
fileObject = open(file_name,'wb')

pickle.dump(clf,fileObject)

data = pd.read_csv("testFood.csv")
df = pd.DataFrame(data)

X_test = df[headers]
Y_test = df["likeCount"]


np.set_printoptions(suppress=True)

pred  = np.ceil(clf.predict(X_test))
org = np.array(Y_test).astype("float32")
err = ((pred-org)/(org+1))*100.0

#orignal and predicted Values
print(org)
print(pred)
print(err)
#Accuracy Scores
print("R^2 Score : ",clf.score(X_test,Y_test))
scores = cross_val_score(clf, X, Y, cv =5)
print("cross_val_score : ",scores)


