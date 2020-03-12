# cromosim

CROMOSIM is a Python Library for Crowd Motion Simulation.

The aim of this open source project is to make it possible to users to run simulations based from several models (cellular automata, microscopic simulations or using compartments), to test new configurations, and even to investigate the possibility to program their own model in complex geometry : do-it yourself !

This package proposes Python implementations of the numerical methods detailed in the book “Crowds in equations: an introduction to the microscopic modeling of crowds” by B. Maury (ENS Ulm & Univ. Paris-Sud) and S. Faure (CNRS), World Scientific 2018, Advanced textbooks in mathematics.

Installation (Python 3)
========================

Reqirements (_added by NM_)
---------

Cromosim appears to need an old version of `scipy` and the `pillow` library (although there is no warnnig if `pillow` is not available, it just crashes). An anaconda environment called `cromosim` has been included that seems to load the correct packages:

```
conda env create -f environment.yml
conda activate cromosim
```

With Pypi
---------

   pip install cromosim

or

   pip install cromosim --user

From source
-----------

You can also clone the project

   git clone https://github.com/sylvain-faure/cromosim/

and then use the command

   python setup.py install


Documentation
=============

http://www.cromosim.fr
