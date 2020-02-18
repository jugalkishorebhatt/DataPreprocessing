# !/usr/bin/python

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

"""
Created on December 11
@author Jugal
"""
class SupervisedLearning:
    "Creates Dataframe for the fixed Length File"
    X_train_40 =[]
    X_validation_40 = []
    Y_train_40 = []
    Y_validation_40 = []
    
    
    "Initializer"
    def __init__(self,data):
        self.data = data
        
    def __TrainTestData(self):
        col = self.data.select_dtypes(['category']).columns
        self.data[col+'_cdx'] = self.data[col].apply(lambda x: x.cat.codes)
        features = self.data[['age', 'job_cdx', 'marital_cdx', 'education_cdx', 'default_cdx','housing_cdx', 'loan_cdx', 'contact_cdx', 'month_cdx','day_of_week_cdx', 'duration', 'campaign', 'pdays', 'previous', 'poutcome_cdx', 'emp_var_rate','cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed']]
        
        target = self.data['y']
        
        SupervisedLearning.X_train_40, SupervisedLearning.X_validation_40, SupervisedLearning.Y_train_40, SupervisedLearning.Y_validation_40 = model_selection.train_test_split(features, target, test_size=0.4, random_state=7)
        SupervisedLearning(self.data).__ModelSelection()
        
    def __ModelSelection(self):    
        seed = 7
        scoring = 'accuracy'

        # Spot Check Algorithms
        algo = []

        algo.append(('KNN', KNeighborsClassifier()))
        algo.append(('DST', DecisionTreeClassifier()))

        # evaluate each model in turn
        results = []
        names = []
        for name, model in algo:
            kfold = model_selection.KFold(n_splits=10, random_state=seed)
            cv_results = model_selection.cross_val_score(model, SupervisedLearning.X_train_40, SupervisedLearning.Y_train_40, cv=kfold, scoring=scoring)
            results.append(cv_results)
            names.append(name)
            msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
            print(msg)
        SupervisedLearning(self.data).__FitPredict()    
    
    def __FitPredict(self):            
            dst = DecisionTreeClassifier(criterion='gini',max_leaf_nodes=8)
            dst.fit(SupervisedLearning.X_train_40, SupervisedLearning.Y_train_40)
            predictions = dst.predict(SupervisedLearning.X_validation_40)
            print("DST Testing Split 40")
            print()
            print(accuracy_score(SupervisedLearning.Y_validation_40, predictions))
            print(confusion_matrix(SupervisedLearning.Y_validation_40, predictions))
            print(classification_report(SupervisedLearning.Y_validation_40, predictions))