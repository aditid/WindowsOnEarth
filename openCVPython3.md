# Installing OpenCV on Python 3

Documentation covers steps necessary to install openCV 2 on a pyenv virtual environment with Python 3.6.1.

Adrian Rosebrock's article [Install OpenCV 3 on macOS with Homebrew (the easy way)](http://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/) and Adam Gradzki's article [Python 3.6, OpenCV 3.2, and PyEnv on macOS Sierra](https://medium.com/@nszceta/python-3-6-opencv-3-2-and-pyenv-on-macos-sierra-6ebcebd6193e) were important references in developing this documentation.

## Pre-Requisites
Before beginning the actual installation of OpenCV, there are multiple frameworks that need to be installed first.

### X-Code
* Opening up the Mac App Store is the easiest way to download X-Code

* Open Terminal and Install Apple Command Line Tools<br />
`$ sudo xcode-select --install`

* Accept the Apple Developer Liscence<br />
`$ sudo xcodebuild -liscence`

### Homebrew
Homebrew is a package manager for macOS that will be used to install OpenCV and other packages.

* Install Homebrew<br />
`$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

* Update Homebrew<br />
`$ brew update`

You will need to update your `~/.bash_profile` file so that it searches your Homebrew path for packages/libraries before it searches your system path. ***This was basically copied from the first article***

* Open the `~/.bash_profile` file from the root directory using your favorite text editor. *Sublime text is used in this example.*<br />
`$ sublime ~/.bash_profile`

* Set path inside of `~/.bash_profile` file<br />
Append the following line to the file:
`export PATH=/usr/local/bin:$PATH`

* Reload file<br />
`$ source ~/.bash_profile`

### Python
The Homebrew version of python will be used over the one that comes with the system.

* Install Python<br />
`$ brew install python3`

* Link Python<br />
`$ brew link python3`

* Check that Python is linked to the correct directory

`$ which python3`<br />
Output should be:<br />
`/usr/local/bin/python3`

### Installing Required Frameworks

`$ brew tap homebrew/science`

`$ brew install eigen tbb hdf5 tesseract pyenv pyenv-virtualenv`

`$ brew install cmake`

### Setting up pyenv Python Virtual Environment
* Install pyenv<br />
`env PYTHON_CONFIGURE_OPTS="--enable-shared" CFLAGS="-O2" pyenv install 3.6.1`

* Add these lines to the `~/.bash_profile` file:<br />
`eval "$(pyenv virtualenv-init -)"`<br />
`eval "$(pyenv init -)"`<br />

* Reload file <br />
`$ source ~/.bash_profile`

* create new pyenv virtual environment<br />
`$ pyenv virtualenv 3.6.1 heal`<br />
**heal** *is the project name*

* Activate the virtual environment<br />
`$ pyenv activate heal`

* Install pip dependencies<br />
`$ pip install -U pip setuptools wheel cython numpy`

Installing OpenCV
-----------------

`$ sudo mkdir -p /opt/src`

`$ sudo chown $(whoami):staff /opt`

`$ sudo chown $(whoami):staff /opt/src`

`$ cd /opt/src`

`$ curl -L https://github.com/opencv/opencv/archive/3.2.0.zip -o opencv32.zip`

`$ curl -L https://github.com/opencv/opencv_contrib/archive/3.2.0.zip -o opencv32contrib.zip`

`$ unzip opencv32.zip`

`$ unzip opencv32contrib.zip`

`$ mv -v opencv-3.2.0 /opt/src/opencv32_py36`

`$ mv -v opencv_contrib-3.2.0 /opt/src/opencv32_py36_contrib`

`$ cd /opt/src/opencv32_py36`

`$ mkdir /opt/src/opencv32_py36/release`

`$ cd /opt/src/opencv32_py36/release`

```
$ cmake \
    -D CMAKE_INSTALL_PREFIX=/opt/opencv32_py36 \
    -D OPENCV_EXTRA_MODULES_PATH=/opt/src/opencv32_py36_contrib/modules \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D BUILD_TIFF=ON \
    -D BUILD_opencv_java=OFF \
    -D WITH_CUDA=OFF \
    -D ENABLE_FAST_MATH=1 \
    -D ENABLE_AVX=ON \
    -D WITH_OPENGL=ON \
    -D WITH_OPENCL=ON \
    -D WITH_IPP=OFF \
    -D WITH_TBB=ON \
    -D WITH_EIGEN=ON \
    -D WITH_V4L=OFF \
    -D WITH_VTK=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D PYTHON3_LIBRARY=$(python3 -c "import re, os.path; print(os.path.normpath(os.path.join(os.path.dirname(re.__file__), '..', 'libpython3.6m.dylib')))") \
    -D PYTHON3_EXECUTABLE=$(which python3) \
    -D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
    -D PYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") ..
```

`$ make -j8`

`$ make install`

Making Sure it Works
--------------------

* Open the Python shell<br />
`$ python3`<br />
It should say the python version number is `3.6.1`.

* In the shell type:<br />
`>>> import opencv2`

If you do not get any errors, then CONGRADULATIONS!! Everything installed properly and you can now use OpenCV!