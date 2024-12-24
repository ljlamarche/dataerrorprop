# errorweight.py
# Error-weighted versions of common data analysis functions
# Error propigation is also applied
# Functions take in both values and an equal sized array of their errors.
# All parameters are assumed to be Gaussian random variables.


import numpy as np

def mean(x, dx, w=None, axis=None):

    # Use inverse of the errors squared for weights if not explictly provide
    if w is None:
        w = dx**(-2)

    mu = np.nansum(w*x, axis=axis)/np.nansum(w, axis=axis)
    dmu = np.sqrt(np.nansum(w**2*dx**2, axis=axis))/np.nansum(w)

    return mu, dmu

def stddev(x, dx, w=None, axis=None):

    # Use inverse of the errors squared for weights if not explictly provide
    if w is None:
        w = dx**(-2)

    mu, dmu = mean(x, dx, w=w, axis=axis)

    M = np.sum(w>0., axis=axis)
    sig = np.sqrt(np.nansum(w*(x-mu)**2, axis=axis)/((M-1)/M*np.nansum(w, axis=axis)))
    dsig = np.sqrt((np.nansum(w**2*(x-mu)**2*dx**2, axis=axis) + np.nansum(w*(x-mu), axis=axis)**2*dmu**2)/((M-1)/M*np.nansum(w, axis=axis)*np.nansum(w*(x-mu)**2, axis=axis)))

    return sig, dsig

def histogram(x, dx):
    return

