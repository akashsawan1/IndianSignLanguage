import pandas as pd
#from numpy._distributor_init import NUMPY_MKL
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
import os


filename = input('Enter the csv file name to read: ')
sub = pd.read_csv(filename)
y_pred = np.array(sub.pop('Label'))
y_test = np.array(sub.pop('TrueLabel'))
path = 'data'

class_labels = []


for (dirpath,dirnames,filenames) in os.walk(path):
    #dirnames.sort()
    for label in dirnames:
            #print(label)
        if not (label == '.DS_Store'):
            class_labels.append(label)
              


def plot_confusion_matrix(cm, labels,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(labels))
    plt.xticks(tick_marks, labels, rotation=45)
    plt.yticks(tick_marks, labels)

    if normalize:
        print("Normalized confusion matrix")
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    else:
        print('Confusion matrix, without normalization')

    print(cm)
    for i in cm:
        a=0
        for j in i:
            a=a+j
        print(a)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, labels=class_labels, title='Confusion matrix, without normalization')
plt.show()