# error_prop.py
# Common data analysis functions with error propigation.
# Functions take in both values and an equal sized array of their errors.
# All parameters are assumed to be Gaussian random variables.


import numpy as np


def mean(x, dx, axis=None):
    '''
    Calculate the average and the error on the average.
    '''

    N = np.sum(np.isfinite(x), axis=axis)
    mu = np.nansum(x, axis=axis)/N
    dmu = np.sqrt(np.nansum(dx**2, axis=axis))/N

    return mu, dmu


def stddev(x, dx):
    '''
    Calculate the standard deviation and the error on the standard deviation.
    '''

    N = np.sum(np.isfinite(x), axis=axis)
    mu, dmu = mean(x, dx)

    sig = np.sqrt(np.nansum((x-mu)**2)/(N-1))
    dsig = np.sqrt((np.nansum((x-mu)**2*dx*2) + np.nansum(x-mu)**2*dmu**2)/((N-1)*np.nansum((x-mu)**2))

    return sig, dsig
