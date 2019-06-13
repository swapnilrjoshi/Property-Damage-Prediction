# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:42:54 2019

@author: srjcp
"""
import numpy as np
from sklearn import base
from sklearn.model_selection import KFold

class KFoldTargetEncoderTrain(base.BaseEstimator, base.TransformerMixin):
    
    def __init__(self, colnames,targetName,n_fold=5,verbosity=True,discardOriginal_col=False):

        self.colnames = colnames
        self.targetName = targetName
        self.n_fold = n_fold
        self.verbosity = verbosity
        self.discardOriginal_col = discardOriginal_col

    def fit(self, X, y=None):
        return self

    def transform(self,X):

        mean_of_target = X[self.targetName].mean()
        kf = KFold(n_splits = self.n_fold, shuffle = False, random_state=47)
        
        return_map = {}
        for col in self.colnames:
            col_mean_name = col + '_' + 'Kfold_Target_Enc'
            X[col_mean_name] = np.nan
            
            for tr_ind, val_ind in kf.split(X):
                X_tr, X_val = X.iloc[tr_ind], X.iloc[val_ind]
                X.loc[X.index[val_ind], col_mean_name] = X_val[col].map(X_tr.groupby(col)[self.targetName].mean())

            X[col_mean_name].fillna(mean_of_target, inplace = True)
            
            return_map[col] = X[[col, col_mean_name]].groupby(col).mean().reset_index() 

            if self.verbosity:            
                encoded_feature = X[col_mean_name].values
                print('Correlation between the new feature, {} and, {} is {}.'.format(col_mean_name,
                                                                                          self.targetName,
                                                                                          np.corrcoef(X[self.targetName].values, encoded_feature)[0][1]))
        if self.discardOriginal_col:
            X = X.drop(self.targetName, axis=1)
            
        return X, return_map


class KFoldTargetEncoderTest(base.BaseEstimator, base.TransformerMixin):
    
    def __init__(self,mapping,colNames):
        
        self.map = mapping
        self.colNames = colNames
                
    def fit(self, X, y=None):
        return self

    def transform(self,X):
        for col in self.colNames:
            mean = self.map[col]
            col_names=list(mean.columns)
            dd = {}
            for index, row in mean.iterrows():
                dd[row[col_names[0]]] = row[col_names[1]]
        
            X[col_names[1]] = X[col_names[0]]
            X = X.replace({col_names[1]: dd})

        return X