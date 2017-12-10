from multiprocessing.pool import ThreadPool
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy
from scipy import misc
import os
from multiprocessing import Pool
from tqdm import tqdm




inputDirectory = '../../BU10000SetAB'
inputFile = './imagePerTag.npy'
tags = np.load(inputFile).item()

images = []
for tag in tags:
    images = sum([images, tags[tag]],[])

images = list(set(images))


directory = '../../NumpyImages'
if not os.path.exists(directory):
    os.makedirs(directory)

def forceLandscape(image):
    if image.shape[0] > image.shape[1]:
        return np.rot90(image)
    return image

def resizeImage(image, x,y):
    return scipy.misc.imresize(image,(x,y), interp='nearest')

def grayscale(image):
    return np.dot(image[...,:3], [0.21, 0.72, 0.07])

def reshape(image):
    return image.flatten()

def formatImage(image):
    image = forceLandscape(image)
    image = resizeImage(image, 64, 64)
    image = grayscale(image)
    image = reshape(image)
    return image

def loadImage(imagePath):
    image = mpimg.imread(imagePath)
    imageFile = imagePath.split('/').pop()
    np.save('../../NumpyImages/' + imageFile, formatImage(image))

p = Pool()
#threads.map(loadImage, positiveImages)
list(tqdm(p.imap(loadImage, images), total=len(images)))
