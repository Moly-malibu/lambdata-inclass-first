#Dataframe nulls

int main()

{
    int*ptr = NULL;

    print(The value of ptr is %u",ptr);

    return 0;

}

#Report Confusion Matrix
# script for confusion matrix creation. 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

actual = [11, 12, 0, 17, 0, 10, 17, 0, 0, 20] 
predicted = [21, 0, 0, 10, 0, 0, 51, 1, 41, 10] 
results = confusion_matrix(actual, predicted)

print 'Confusion Matrix :'
print(results) 
print 'Accuracy Score :',accuracy_score(actual, predicted) 
print 'Report : '
print classification_report(actual, predicted) 