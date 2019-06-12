
Construction du corpus
======================
Parser les fichiers XML, puis selectionner les balises qui correspondent au token de l'abstract
 les token sont déjà lemmatisés

Corpus discovery
==========================
- Word cloud
- T-SNE
- Class repartition (chart bar)
- Lexical richness measures


![word_cloud](resources/word_cloud.png)

![t-sne](resources/tsne_preprocessed.png)

![class_distribution](resources/labels_barchart.png)

    Abstract number: 7822
    Vocabulary size:  10178
    Corpus size:  492143
    Vocabulary richness:  0.020680980934403213
    Abstract Mean words:  62.91779596011251
    Number of class 39

Préparation des données
=======================
- Tokenization (Deja lemmatisé dans le dataset brut)
- Suppression des stopwords (les stops word sont tous les termes qui ne figurent pas dans la liste de vocabulaire médical)

Resources
=========
 - Biomedical vocabulary used in addition to stop word list, all word not in vocabulary are removed
    
BioMedical vocabulary
===================
l'idée est de garder que les tremes médicaux qui ont un réel impact sur la classification de l'abstract
Il s'agit d'une simple liste de termes médicaux anglais formatés sous la forme d'un fichier texte codé en UTF8.
Il est basé sur deux projets de dictionnaire médical de premier plan:
    1. OpenMedSpel par e-MedTools
    2. Raj & Co-Med-Spel-Chek par Rajasekharan N. de Raj & Co
disponible sur le lien suivant: https://github.com/glutanimate/wordlist-medicalterms-en


Représentation des mots
=======================
- word embedding (not tested beacause of my machine perfomance)
- tf-idf
- bag of word


Interprétation des résultats d'Apprentissage
============================================

Modèles utilisés pour la classification de texte (multiclasse)
    - SVC
    - SVC linéaire
    - Naive Bayes MultinomialNB

Validation du modèle
    - validation en 85% train et 15% test 
    - validation croisée
    
Résultats
    
    Naive Bayes Classification Accuracy : 21.63543441226576
    SVM classification Accuracy : 0.20528109028960817 
    
    Accuracy score cross validation (SVC - Multi-class classifier one-vs-one) 
    [0.6079182630906769, 0.5849297573435505, 0.5843989769820972, 0.59846547314578, 0.6010230179028133, 0.5613810741687979, 0.5895140664961637, 0.6010230179028133, 0.6061381074168798, 0.5818414322250639]
    Accuracy score cross validation (SVC - Multi-class classifier one-vs-the-rest)
    [0.5938697318007663, 0.5721583652618135, 0.5946291560102301, 0.5997442455242967, 0.6202046035805626, 0.5485933503836317, 0.6035805626598465, 0.5959079283887468, 0.5971867007672634, 0.5882352941176471]
    
    Report SVM
    
    precision    recall  f1-score   support

           0       0.00      0.00      0.00         0
           1       0.00      0.00      0.00         0
           2       0.84      0.47      0.60       146
           3       0.80      0.26      0.39       317
           4       0.00      0.00      0.00         0
           5       0.97      0.44      0.61       229
           6       0.00      0.00      0.00         0
           7       0.02      0.01      0.01       130
           8       0.00      0.00      0.00        44
           9       0.00      0.00      0.00        42
          10       0.01      0.17      0.03         6
          11       0.00      0.00      0.00        71
          12       0.00      0.00      0.00         0
          13       0.00      0.00      0.00        66
          14       0.00      0.00      0.00         3
          15       0.00      0.00      0.00         0
          16       0.00      0.00      0.00         0
          17       0.00      0.00      0.00         0
          18       0.00      0.00      0.00        18
          19       0.00      0.00      0.00         0
          20       0.00      0.00      0.00         0
          21       0.00      0.00      0.00         0
          22       0.00      0.00      0.00         0
          23       0.00      0.00      0.00         0
          24       0.00      0.00      0.00         0
          25       0.00      0.00      0.00         9
          26       0.00      0.00      0.00         7
          27       0.00      0.00      0.00         0
          28       0.00      0.00      0.00         0
          29       0.00      0.00      0.00         0
          30       0.00      0.00      0.00         0
          31       0.00      0.00      0.00         0
          32       0.00      0.00      0.00         0
          33       0.00      0.00      0.00         0
          34       0.00      0.00      0.00         0
          35       0.00      0.00      0.00         0
          36       0.00      0.00      0.00         0
          37       0.04      0.01      0.02        86

    accuracy                           0.22      1174


Interprétation
--------------
7822 abstract pour 39 classes, trop peu de données

La répartition des classes est déséquilibrée, par conséquent le modèle a appris sur quelques classes qui sont représentées  
par plusieurs intances, le modèle n'a pas été capable d'apprendre sur les classes sous représentée




    
    