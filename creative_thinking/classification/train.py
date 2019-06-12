import pickle

import numpy as np
from sklearn import model_selection, naive_bayes, svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

np.random.seed(500)

corpus = pickle.load(open('../dataset/preprocessed_eng_dataset.pickle', 'rb'))
X = corpus['text_final']
y = corpus['tag']

# Make sure that all of train set and test set get the same ratio of classes
kf = KFold(n_splits=37, random_state=0, shuffle=True)
for train_index, test_index in kf.split(y):
    Train_X, Test_X = X[train_index], X[test_index]
    Train_Y, Test_Y = y[train_index], y[test_index]

Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(corpus['text_final'], corpus['tag'],
                                                                    stratify=corpus['tag'],
                                                                    test_size=0.15)
# encode labels
Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(Train_Y)
Test_Y = Encoder.fit_transform(Test_Y)

# tf-idf representation
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(corpus['text_final'])
Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)
# print(Tfidf_vect.vocabulary_)


#########################
# fit the NB classifier #
#########################
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf, Train_Y)
# prediction
predictions_NB = Naive.predict(Test_X_Tfidf)
# accuracy_score
print("Naive Bayes Classification report -> ")
print(classification_report(predictions_NB, Test_Y) * 100)

##########################
# fit the SVM classifier #
##########################
# Multi-class classifier one-vs-one
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf, Train_Y)
# prediction
predictions_SVM = SVM.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("SVM classification report -> ")
print(classification_report(predictions_SVM, Test_Y))

#########################
# SVC - Cross validation#
#########################
X = Tfidf_vect.transform(corpus['text_final'])
y = Encoder.fit_transform(corpus['tag'])
scores_svc = []
best_svm = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
cv = KFold(n_splits=10, random_state=42, shuffle=False)

for train_index, test_index in cv.split(X):
    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    best_svm.fit(X_train, y_train)
    prediction = best_svm.predict(X_test)
    scores_svc.append(accuracy_score(prediction, y_test))
print("SVC - Multi-class classifier one-vs-one")
print(scores_svc)

##########################################
# Multi-class classifier one-vs-the-rest##
##########################################
scores_lin_svc = []
lin_clf = svm.LinearSVC()
cv = KFold(n_splits=10, random_state=42, shuffle=False)

for train_index, test_index in cv.split(X):
    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    lin_clf.fit(X_train, y_train)
    prediction = lin_clf.predict(X_test)
    scores_lin_svc.append(accuracy_score(prediction, y_test))
print("SVC - Multi-class classifier one-vs-the-rest")
print(scores_lin_svc)
