# error_prop.py
# Common data analysis functions with error propigation.
# Functions take in both values and an equal sized array of their errors.
# All parameters are assumed to be Gaussian random variables.


import numpy as np


def mean(x, s, axis=None):
    '''
    Calculate the average and the error on the average.
    '''

    N = np.sum(np.isfinite(x), axis=axis)
    mu = np.nansum(x, axis=axis)/N
    sig = np.sqrt(np.nansum(s**2, axis=axis))/N

    return mu, sig


def stddev(x, dx):
    '''
    Calculate the standard deviation and the error on the standard deviation.
    '''
    return
