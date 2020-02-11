from sklearn.metrics import plot_confusion_matrix

#Dataframe nulls

df.isnull()

#print report

import pandas_profiling
df.profile_reporte()

#Report Confusion Matrix:

# Check scikit-learn version
import sklearn
sklearn.__version__

y_true = [1, 0, 1, 2, 0, 1]
y_pred = [0, 1, 2, 1, 0, 0]
confusion_matrix(y_true, y_pred)

plot_confusion_matrix(pipeline, y_true, y_pred, values_format='.0f', xticks_rotation='vertical');