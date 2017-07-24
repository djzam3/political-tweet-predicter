from sklearn import svm, datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
import itertools

def trainSVM(data, target):
	clf = svm.SVC(kernel='linear', gamma='auto', probability=True)
	clf.fit(data, target)
	joblib.dump(clf, "classifier012.pkl") #store classifier
	print("SVM trained")

def trainNB(data, target):
	gnb = GaussianNB()
	clf = gnb.fit(data, target)
	joblib.dump(clf, "classifier012.pkl")
	print("Naive Bayes trained")

def predictProb(datum):
	b = joblib.load("classifier012.pkl") #load trained classifer
	return(b.predict_proba([datum]))

def predict(datum):
	b = joblib.load("classifier012.pkl") #load trained classifer
	return(b.predict([datum]))

def show(data, target):
	
	X = data[:, :2] 
	y = target

	h = .10  # step size in the mesh

	# we create an instance of SVM and fit out data. We do not scale our
	# data since we want to plot the support vectors
	C = 1.0  # SVM regularization parameter
	svc = svm.SVC(kernel='linear', C=C).fit(X, y)
	
	# create a mesh to plot in
	x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
	y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
	xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
			     np.arange(y_min, y_max, h))

	# Plot the decision boundary. For that, we will assign a color to each
	# point in the mesh [x_min, x_max]x[y_min, y_max].
	plt.plot(20, 20)
	
	Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

	# Put the result into a color plot
	Z = Z.reshape(xx.shape)
	plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

	# Plot also the training points
	plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
	plt.xlabel('Superlative')
	plt.ylabel('Numeral')
	plt.xlim(xx.min(), xx.max())
	plt.ylim(yy.min(), yy.max())
	plt.xticks(())
	plt.yticks(())
	plt.title('SVC with linear kernel')

	plt.show()

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
	"""
	This function prints and plots the confusion matrix.
	Normalization can be applied by setting `normalize=True`.
	"""
	plt.imshow(cm, interpolation='nearest', cmap=cmap)
	plt.title(title)
	plt.colorbar()
	tick_marks = np.arange(len(classes))
	plt.xticks(tick_marks, classes, rotation=45)
	plt.yticks(tick_marks, classes)

	if normalize:
		cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
		print("Normalized confusion matrix")
	else:
		print('Confusion matrix, without normalization')

	print(cm)

	thresh = cm.max() / 2.
	for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
		plt.text(j, i, cm[i, j],
		horizontalalignment="center",
		color="white" if cm[i, j] > thresh else "black")

	plt.tight_layout()
	plt.ylabel('True label')
	plt.xlabel('Predicted label')


def train_conf(data, target):
	class_names = np.array(['NV', 'v', 'VV'])
	X = data
	y = target
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

	clsfr = svm.SVC(kernel='linear', C=0.01)
	y_pred = clsfr.fit(X_train, y_train).predict(X_test)
	cnf_matrix = confusion_matrix(y_test, y_pred)
	np.set_printoptions(precision=2)

	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=class_names, title='Confusion matrix')
	plt.show()

