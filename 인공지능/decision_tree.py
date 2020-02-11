# AI homework by sangmin
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import os

report1 = pd.read_csv("C:/Users/sangmin/Desktop/code/DKU_git/인공지능/dstest.csv")
X = np.array(pd.DataFrame(report1, columns=['X','y']))
y = np.array(pd.DataFrame(report1, columns=['C']))
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8)

dt_clf = DecisionTreeClassifier(criterion='entropy')
dt_clf = dt_clf.fit(X_train, y_train)
y_train_pred = dt_clf.predict(X_train)
y_test_pred = dt_clf.predict(X_test)
tree_train = accuracy_score(y_train, y_train_pred)
tree_test = accuracy_score(y_test, y_test_pred)
print('[Default] \t train accuracy %.3f \n\t\t test accuracy %.3f' % (tree_train, tree_test))
print('\n')

# max_depth
num = 2;
for i in range(5): 
    dt_clf = DecisionTreeClassifier(criterion='entropy', max_depth = num)
    dt_clf = dt_clf.fit(X_train, y_train)
    y_train_pred = dt_clf.predict(X_train)
    y_test_pred = dt_clf.predict(X_test)
    tree_train = accuracy_score(y_train, y_train_pred)
    tree_test = accuracy_score(y_test, y_test_pred)
    print('[max_depth=%d]    train accuracy %.3f \n\t\t test accuracy %.3f' % (num, tree_train, tree_test))
    num += 1
print('\n')

# min_samples_split
num = 250
for i in range(10):
    dt_clf = DecisionTreeClassifier(criterion='entropy', min_samples_split = num)
    dt_clf = dt_clf.fit(X_train, y_train)
    y_train_pred = dt_clf.predict(X_train)
    y_test_pred = dt_clf.predict(X_test)
    tree_train = accuracy_score(y_train, y_train_pred)
    tree_test = accuracy_score(y_test, y_test_pred)
    print('[min_split=%d]    train accuracy %.3f \n\t\t test accuracy %.3f' % (num, tree_train, tree_test))
    num += 10
print('\n')

# min_samples_leaf
num = 10
for i in range(10):
    dt_clf = DecisionTreeClassifier(criterion='entropy', min_samples_leaf = num)
    dt_clf = dt_clf.fit(X_train, y_train)
    y_train_pred = dt_clf.predict(X_train)
    y_test_pred = dt_clf.predict(X_test)
    tree_train = accuracy_score(y_train, y_train_pred)
    tree_test = accuracy_score(y_test, y_test_pred)
    print('[min_leaf=%d]    train accuracy %.3f \n\t\t test accuracy %.3f' % (num, tree_train, tree_test))
    num += 5
