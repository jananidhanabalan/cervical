import pandas as pd
import numpy as np
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import BorderlineSMOTE
from matplotlib import pyplot
from numpy import where
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, f1_score, recall_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split



def pre_process(test, seed):
    np.random.seed(seed)
    df = pd.read_csv("Clean Data_2.csv")
    df.drop('Unnamed: 0', inplace=True, axis=1)
    X = df.drop(['Hinselmann', 'Schiller', 'Citology', 'Biopsy'], axis=1).values
    y = df[test].values
    oversample = BorderlineSMOTE()
    X, y = oversample.fit_resample(X, y)
    clf = ExtraTreesClassifier(n_estimators=50)
    clf = clf.fit(X, y)
    model = SelectFromModel(clf, prefit=True)
    X_new = model.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=101)
    return X_train, X_test, y_train, y_test


def hinselmann_model():
    X_train, X_test, y_train, y_test = pre_process('Hinselmann', 7)
    param_grid = {'C': [10], 'gamma': [1]}
    grid = GridSearchCV(SVC(), param_grid, verbose=3)
    grid.fit(X_train, y_train)
    return grid

def schiller_model():
    X_train, X_test, y_train, y_test = pre_process('Schiller', 0)
    rfc = RandomForestClassifier(n_estimators=200)
    rfc.fit(X_train,y_train)    
    return rfc

def citology_model():
    X_train, X_test, y_train, y_test = pre_process('Citology', 0)
    param_grid = {'C': [10], 'gamma': [1]}
    grid = GridSearchCV(SVC(), param_grid, verbose=3)
    grid.fit(X_train, y_train)
    return grid

def biopsy_model():
    X_train, X_test, y_train, y_test = pre_process('Biopsy', 2)
    rfc = RandomForestClassifier(n_estimators=200)
    rfc.fit(X_train,y_train)    
    return rfc



