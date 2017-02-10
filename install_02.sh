#! /bin/bash

# Creating environment (sandbox instance called py2 [choose the name you want])
conda create -n py27 python=2.7 jupyter

# Activating created environment
source activate py27

# Install package manager pip
conda install pip

# which ipython is to be used in the environment? pip freeze shows it
pip freeze

# Installing ipython notebook
#conda install jupyter
conda install nose
conda install pytest