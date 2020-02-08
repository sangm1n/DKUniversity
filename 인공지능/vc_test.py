import numpy as np
import pandas as pd
import pylab as plt

from sklearn.model_selection import KFold,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv('pima-indians-diabetes.csv', names=names)
X = df.values[:, 0:8]
y = df.values[:, 8]

# scale X
scl = StandardScaler()
X = scl.fit_transform(X)

# set a 10-fold cross validation
n_splits = 10
kfold = KFold(n_splits=n_splits)

# create the models
estimators = []
clf1 = LogisticRegression()
estimators.append(('logistic', clf1))
clf2 = DecisionTreeClassifier()
estimators.append(('dtree', clf2))
clf3 = SVC(probability=True)
estimators.append(('svm', clf3))

# create the ensemble model
hard_ensemble = VotingClassifier(estimators, voting='hard')
soft_ensemble = VotingClassifier(estimators, voting='soft', weights=[.3, .3, .4])
for clf, label in zip([clf1, clf2, clf3, hard_ensemble, soft_ensemble], ['logistic', 'dtree', 'svm', 'hard ensemble', 'soft ensemble']):
    scores = cross_val_score(clf, X, y, cv=kfold)
    print('Accuracy: %.2f (+/- %.2f) [%s]' % (scores.mean(), scores.std(), label))
