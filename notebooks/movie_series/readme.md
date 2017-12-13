# Installation instructions


To install MacPorts:
```
curl -O https://distfiles.macports.org/MacPorts/MacPorts-2.4.2.tar.bz2  
tar xf MacPorts-2.4.2.tar.bz2  
cd MacPorts-2.4.2/  
./configure  
make  
sudo make install  
```

More details can be found here:
https://guide.macports.org/chunked/installing.macports.html


To install pyentropy: 
```
sudo port install gsl  
python setup.py install
```
