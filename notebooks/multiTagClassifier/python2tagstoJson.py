import glob
import iptcinfo
import numpy as np


inputDirectory = '../../BU10000SetAB'
tags = {}

imagePaths = glob.glob(inputDirectory + "/*.jpg")

for imagePath in imagePaths:
    keywords = iptcinfo.IPTCInfo(imagePath).keywords
    for keyword in keywords:
        if tags.get(keyword,None) is None:
            tags[keyword] = []
        tags[keyword].append(imagePath)

np.save('imagePerTag.json', tags);