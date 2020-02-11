# AI homework by sangmin
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pylab as plt
import os
import warnings
warnings.filterwarnings('ignore')

report1 = pd.read_csv("C:/Users/sangmin/Desktop/code/DKU_git/인공지능/dstest.csv")
X = np.array(pd.DataFrame(report1, columns=['X','y']))
y = np.array(pd.DataFrame(report1, columns=['C']))
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size = 0.8)

est = 10;
for i in range(9):
    ran = RandomForestClassifier(n_estimators=est, criterion='entropy',
                                  max_depth=2, min_samples_split=10,
                                  min_samples_leaf=10, max_leaf_nodes=100,
                                  bootstrap=True)
    ran.fit(X_train, y_train)
    y_train_pred = ran.predict(X_train)
    y_test_pred = ran.predict(X_test)
    ran_train = accuracy_score(y_train, y_train_pred)
    ran_test = accuracy_score(y_test, y_test_pred)
    print('%d est RandomForest train/test accuracies %.3f/%.3f' % (est,ran_train, ran_test))
    est = est+5;