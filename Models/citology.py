import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import BorderlineSMOTE
from numpy import where
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, f1_score, recall_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split

def citology_model():
    print('Citology')


    np.random.seed(0)

    df = pd.read_csv("Clean Data_2.csv")

    df.drop('Unnamed: 0',inplace=True,axis=1)

    # define dataset
    X = df.drop(['Hinselmann','Schiller','Citology','Biopsy'],axis=1).values
    y = df['Citology'].values

    # transform the dataset
    oversample = BorderlineSMOTE()
    X, y = oversample.fit_resample(X, y)

    clf = ExtraTreesClassifier(n_estimators=50)
    clf = clf.fit(X, y)

    features = ['Age', 'Number of sexual partners', 'First sexual intercourse',
        'Num of pregnancies', 'Smokes', 'Smokes (years)', 'Smokes (packs/year)',
        'Hormonal Contraceptives', 'Hormonal Contraceptives (years)', 'IUD',
        'IUD (years)', 'STDs', 'STDs (number)', 'STDs:condylomatosis',
        'STDs:syphilis', 'STDs:HIV', 'STDs: Number of diagnosis', 'Dx:Cancer',
        'Dx:CIN', 'Dx:HPV', 'Dx']

    feat_importances = pd.Series(clf.feature_importances_, index=features)

    print(feat_importances.sort_values())

    model = SelectFromModel(clf, prefit=True)

    X_new = model.transform(X)

    print(X_new.shape)

    X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=101)

    param_grid = {'C': [10], 'gamma': [1]}
    grid = GridSearchCV(SVC(), param_grid, verbose=3)
    grid.fit(X_train, y_train)
    predictions = grid.predict(X_test)
    print("Accuracy: ", accuracy_score(y_test,predictions))
    print("Precision: ", precision_score(y_test,predictions))
    print("Recall: ", recall_score(y_test,predictions))
    print("F-1: ", f1_score(y_test,predictions))

    print("\n")
    print(classification_report(y_test,predictions))
    print("\n")
    print(confusion_matrix(y_test,predictions))

    return grid

citology_model()