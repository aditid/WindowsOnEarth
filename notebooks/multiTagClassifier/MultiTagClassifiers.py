
# coding: utf-8

# In[23]:


import numpy as np
from multiprocessing import Pool
from sklearn.model_selection import cross_validate
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB


# In[24]:


datasetPath = '../../NumpyImages/'
tagFile = './imagePerTag.npy'


# In[25]:


#Constants
classes = ['Moon','Day','ISS Structure','Volcano','Surface','Sun','Agriculture','Solar Panels','Inside ISS','Aurora','Clouds','Night','Atmosphere','Spacecraft','Deployed satellite','Movie','Hurricane','Solar Eclipse','Cupola','Dock Undock']


# In[36]:


tags = np.load(tagFile).item()
tagList = tags.keys()


# In[27]:


def convertFilePath(imageList):
    images = []
    for img in imageList:
        imageFileName = img.split('/').pop()
        imageFileName += '.npy'
        images.append(imageFileName)
    return images


# In[28]:


def loadImagesForTag(tag):
    positiveImages = tags[tag]
    negtiveImages = []
    for negitiveTag in tags:
        if(negitiveTag != tag):
            negtiveImages = sum([negtiveImages,tags[negitiveTag]],[])
    positiveImages = set(positiveImages)
    negtiveImages = set(negtiveImages)
    negtiveImages = negtiveImages - positiveImages
    return convertFilePath(list(positiveImages)), convertFilePath(list(negtiveImages))


# In[29]:


def loadDataSet(positiveImages,negtiveImages):
    X = []
    y = []
    for positiveImage in positiveImages:
        X.append(np.load(datasetPath + positiveImage))
        y.append('true')
        
    for negtiveImage in negtiveImages:
        X.append(np.load(datasetPath + negtiveImage))
        y.append('false')
        
    return X,y


# In[30]:


names = ["Nearest Neighbors", 
         #"Linear SVM", 
         #"RBF SVM", 
         #"Gaussian Process",
         "Decision Tree", 
         "Random Forest", 
         "Neural Net", 
         "AdaBoost",
         "Naive Bayes",
         "SVM",
         #"QDA"
        ]

classifiers = [
    KNeighborsClassifier(3),
    #SVC(kernel="linear", C=0.025, probability=True),
    #SVC(gamma=2, C=1, probability=True),
    #GaussianProcessClassifier(1.0 * RBF(1.0)), #This took forever and only returned 12%
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    SVC(probability=True)
    #QuadraticDiscriminantAnalysis() # Did not converage
]


# In[31]:


def classify(tag,X,y):
    lines = []
    for name, clf in zip(names, classifiers):
        scores = cross_validate(clf, X,y, cv=5)
        print(tag, scores)
        mean = scores['test_score'].mean()
        std = scores['test_score'].std() * 2
        print(tag + ', ' + name + ', ' + str(mean) + ', ' + str(std))
        lines.append(tag + ', ' + name + ', ' + str(mean) + ', ' + str(std))
    return lines


# In[32]:


def testTag(tag):
    pos, neg = loadImagesForTag(tag)
    X,y = loadDataSet(pos,neg)
    return classify(tag,X,y)


# In[33]:


p = Pool()
results = list(p.imap(testTag, classes))
print(results)

