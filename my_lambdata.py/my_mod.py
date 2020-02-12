#Dataframe for nulls

if null_variable is None:
    print('null_variable is None')
else:
    print('null_variable is not None')
if not_null_variable is None:
    print('not_null_variable is None')
else:
    print('not_null_variable is not None')

#Report Confusion Matrix
# script for confusion matrix creation. 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

def report(actual, predicted):
    results = confusion_matrix(actual, predicted)
    print 'Confusion Matrix :'
    print(results) 
    print 'Accuracy Score :',accuracy_score(actual, predicted) 
    print 'Report : '
    print classification_report(actual, predicted)