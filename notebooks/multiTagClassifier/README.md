# Multi Tag supervised Learning Classification

Use Python 2 to extract tags versios images on the large dataset. The large dataset must be combined into a single directory. 
Run [python2tagstoJson.py](https://github.com/gregfrasco/WindowsOnEarth/blob/master/notebooks/multiTagClassifier/python2tagstoJson.py) to create [imagePerTag.npy](https://github.com/gregfrasco/WindowsOnEarth/blob/master/notebooks/multiTagClassifier/imagePerTag.npy) which is a binary dictionary file.

Use Python 3 to prepere images. Using [prepareImages.py](https://github.com/gregfrasco/WindowsOnEarth/blob/master/notebooks/multiTagClassifier/prepareImages.py) to create a directory of binaray 64x64 grayscale 1-D image vectors. These files will be the input to a classifier.

[MultiTagClassifiers.ipynb](https://github.com/gregfrasco/WindowsOnEarth/blob/master/notebooks/multiTagClassifier/MultiTagClassifiers.ipynb) was used to make the Python file [MultiTagClassifiers.py](https://github.com/gregfrasco/WindowsOnEarth/blob/master/notebooks/multiTagClassifier/MultiTagClassifiers.py) to be run on the scc.

Shared Computer Center Job Settings:
```bash
#!/bin/bash -l

# Set SCC project
#$ -P cs542

# Request a node with at least 8 GB of memory per core 
#$ -l mem_per_core=16G

# Request four cores
#$ -pe omp 16

#$ -m ea

#$ -j y

#$ -N Multitag

module load python/3.6.2
pip install -U --user scikit-learn
python MultiTagClassifiers.py
```

The scc produced these [results.csv](https://github.com/gregfrasco/WindowsOnEarth/blob/master/notebooks/multiTagClassifier/results.csv)