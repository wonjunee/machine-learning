"""
===================================================
Faces recognition example using eigenfaces and SVMs
===================================================

The dataset used in this example is a preprocessed excerpt of the
"Labeled Faces in the Wild", aka LFW_:

  http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

  .. _LFW: http://vis-www.cs.umass.edu/lfw/

  original source: http://scikit-learn.org/stable/auto_examples/applications/face_recognition.html


This iterative version is to see the changes to F1 score as n_components value increases
"""



print __doc__

from time import time
import logging
import pylab as pl
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


###############################################################################
# Download the data, if not already on disk and load it as numpy arrays
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape
np.random.seed(42)

# for machine learning we use the data directly (as relative pixel
# position info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print "Total dataset size:"
print "n_samples: %d" % n_samples
print "n_features: %d" % n_features
print "n_classes: %d" % n_classes


###############################################################################
# Split into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

###############################################################################
# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
# dataset): unsupervised feature extraction / dimensionality reduction
n_components_list = [10, 15, 25, 50, 100, 250]

for n_components in n_components_list:
  print "Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0])
  t0 = time()
  pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)
  print "done in %0.3fs" % (time() - t0)

  eigenfaces = pca.components_.reshape((n_components, h, w))

  print "Projecting the input data on the eigenfaces orthonormal basis"
  t0 = time()
  X_train_pca = pca.transform(X_train)
  X_test_pca = pca.transform(X_test)
  print "done in %0.3fs" % (time() - t0)

  print "\npca variances"
  print pca.explained_variance_ratio_[:2]

  ###############################################################################
  # Train a SVM classification model

  print "Fitting the classifier to the training set"
  t0 = time()
  param_grid = {
           'C': [1e3, 5e3, 1e4, 5e4, 1e5],
            'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
            }
  # for sklearn version 0.16 or prior, the class_weight parameter value is 'auto' from 'balanced'
  clf = GridSearchCV(SVC(kernel='rbf', class_weight='auto'), param_grid)
  clf = clf.fit(X_train_pca, y_train)
  print "done in %0.3fs" % (time() - t0)
  print "Best estimator found by grid search:"
  print clf.best_estimator_


  ###############################################################################
  # Quantitative evaluation of the model quality on the test set

  print "Predicting the people names on the testing set"
  t0 = time()
  y_pred = clf.predict(X_test_pca)
  print "done in %0.3fs" % (time() - t0)

  print classification_report(y_test, y_pred, target_names=target_names)
  print confusion_matrix(y_test, y_pred, labels=range(n_classes))
