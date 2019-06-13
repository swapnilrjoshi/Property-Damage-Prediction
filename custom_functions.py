# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:46:32 2019

@author: srjcp
"""
import xgboost as xgb
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import matplotlib.pylab as plt

#Creating Choropleth Maps
def choroplethMap(df,col,title,cmap='OrRd',figsize=(15,8)):
    '''
    This function creates choropleth map of input feature
    Inpute Parameters:
        df:Input DataFrame
        col:Feature Name from dataframe to plot choropleth map
        title:  Title of choropleth map 
        cmap: (Optional) Color map Default:'OrRd'
        figsize: (Optional) figure size Default:(15,8)
    Returns:
        Choropleth Map
    '''
    fig, ax = plt.subplots(figsize=figsize)
    df.plot(column=col,ax=ax, cmap=cmap, edgecolor='black',linewidth=0.5)
    for idx, row in df.iterrows():
        plt.annotate(text=row['STATE_ABBR'], xy=row['coords'], horizontalalignment='center',size=8)
    ax.set_title(title, fontsize=16)
    ax.set_axis_off()
    # Create colorbar    
    vmin = df[col].min()
    vmax = df[col].max()
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    fig.colorbar(sm)

#Converting Magnitude into 3 different feature
def magnitude_feature(df):
    '''
    This function convert magnitude feature into 3 different feature.
    Whereever Magnitude unit is in. it assigns 1 to that otherwise 0.
    Similarly, when it is in kt. it creates a new feature assigns 1 or 0.
    If it is null assign 1 to that positions in a seperate column.
    '''
    mag = df.split()
    if len(mag)>0 and mag[1]=='kts.':
        x=0
        y = float(mag[0])
        z=0
    elif len(mag)>0 and mag[1]=='in.':
        x=float(mag[0])
        y=0
        z=0
    else:
        x,y,z =0, 0, 1
    return x,y,z

def modelfit(alg, dtrain, ytrain,useTrainCV=True, cv_folds=5, early_stopping_rounds=50):
    
    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(dtrain.values, label=ytrain.values)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
                          metrics='auc', early_stopping_rounds=early_stopping_rounds)
        alg.set_params(n_estimators=cvresult.shape[0])

    alg.fit(dtrain, ytrain,eval_metric='auc')
    return alg

def get_modelReport(ytrue,ypred,yproba):
    cm = confusion_matrix(ytrue, ypred)
    accuracy = metrics.accuracy_score(ytrue,ypred)
    auc = metrics.roc_auc_score(ytrue, yproba[:,1])
    recall_score = metrics.recall_score(ytrue, ypred)
    precision, recall, _ = metrics.precision_recall_curve(ytrue, yproba[:, 1]) 
    pr_auc = metrics.auc(recall, precision)
    #Print model report:
    print("\nModel Report")
    print("Accuracy : {:.4}" .format(accuracy))
    print("AUC Score : {:.4}" .format(auc))
    print("PR AUC Score : {:.4}" .format(pr_auc))
    print("Recall Score : {:.4}" .format(recall_score))
    print("Confusion Matrix :\n{}" .format(cm))
#    return cm,accuracy,auc,recall
