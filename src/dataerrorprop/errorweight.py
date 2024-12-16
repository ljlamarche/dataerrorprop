# errorweight.py
# Error-weighted versions of common data analysis functions
# Error propigation is also applied
# Functions take in both values and an equal sized array of their errors.
# All parameters are assumed to be Gaussian random variables.


import numpy as np

def mean(x, s, axis=None):

    mu = np.nansum(x/s**2, axis=axis)/np.nansum(s**-2, axis=axis)
    sig = np.sqrt(1./np.nansum(s**-2, axis=axis))

    return mu, sig

def stddev(x, dx):
    return

def histogram(x, dx):
    return

