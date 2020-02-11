# AI homework by sangmin
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

report1 = pd.read_csv("C:/Users/sangmin/Desktop/code/DKU_git/인공지능/dstest.csv")
X = np.array(pd.DataFrame(report1, columns=['X','y']))
y = np.array(pd.DataFrame(report1, columns=['C']))
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size = 0.8)

est = 10;
for i in range(9):
    ada = AdaBoostClassifier(n_estimators=est, random_state = 5)
    ada.fit(X_train, y_train)
    y_train_pred = ada.predict(X_train)
    y_test_pred = ada.predict(X_test)
    ada_train = accuracy_score(y_train, y_train_pred)
    ada_test = accuracy_score(y_test, y_test_pred)
    print('%d est AdaBoost train/test accuracies %.3f/%.3f' % (est, ada_train, ada_test))
    est = est +5;