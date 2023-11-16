#!/bin/sh

pip install igfold
git clone git@github.com:Graylab/IgFold.git
pip install IgFold

# Refinement
conda install -c conda-forge openmm==7.7.0 pdbfixer

# Renumbering
conda install -c bioconda abnumber
