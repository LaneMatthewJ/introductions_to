# Getting Started

In order to get started working on big datasets with pandas, you'll need to have python and a handful of other packages. You can work with pandas with either python 3 or python 2, but I would recommend downloading python 3 (given that it's newer, and is not being retired anytime soon like python 2 is). 



## Installation

### The easy way: 

If you're up for a one stop shop with downloading a specific version of python  as well as getting the vast majority of packages required to work with large datasets (along with creating visualizations), you can get everything from using the [anaconda installer](https://www.anaconda.com/distribution/). Make sure you download the installer for the correct os. 

### The slightly less easy way:

If you're interested in downloading python and the corresponding packages individually, first check to see if you already have python installed on your machine.  Many, if not most computers come with python preinstalled. To ensure that python is installed on your machine, type: 

**Windows:**

```powershell
C:\Users\<YOUR USERNAME>python --version
```

**Mac:**

```bash
python --version
```

You should receive a message either says `command not found` OR something that looks akin to: 

```shell
Python 2.7.3 :: Continuum Analytics, Inc.
```

OR

```shell
Python 3.7.3
```

If you recieved a version number, you're all set and you don't need to install python (skip down to the installing jupyter portion). 



#### Installing python: 

You can download the latest version of python (or previous versions, but it's always good to go witht he latest) at [python's website.](https://www.python.org)  You can download the binaries, but, again, I would recommend downloading the installer given that it's much easier to work with. 

Once you've finished downloading the installer, run it. Once finished, open a new terminal and try typing: 

**Windows:**

```powershell
C:\Users\<YOUR USERNAME>python --version
```

**Mac:**

```bash
python --version
```

If these commands don't return a version number then try restarting your machine. (If they continue to not return a version number, try reinstalling python). 



#### Installing jupyter: 

In order to work with most of our material, you'll need to have an iPython notebook reader. I personally work with jupyter, but if you would like to work with iPython (an older version of jupyter), that's fine too, but you may likely run into errors. You can install the pacakage for the notebook reader by typing: 

```bash
pip install --upgrade pip  ## This updates your pip
pip install jupyter
```

If the above code does not work, try rerunning it with `pip3` instead of `pip`. 





## Working with Jupyter notebooks. 

To open a jupyter notebook session, open your terminal and navigate to the folder that you'd like to work in. Once there, enter: 

```bash
jupyter notebook
```

A web browser ought to pop up taking you to ` http://localhost:8888/tree`. From here, you can use the GUI to create new notebooks. 



#### Creating a new notebook && running code: 

On the righthand side of the screen, click the `new` menu and under `Notebook:` select the kernel (for our purposes, you'll likely only have Python 3). Once inside the new notebook, you can rename it. 

In order to run each individual cell of the notebook after writing code, use either the keyboard command `shift + enter` , or to add a new code box below the space you're running your code, enter the command `alt + shift + enter`. 
