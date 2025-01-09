# weighted.py
# Weighted versions of common data analysis functions that account for error propogation.
# If no explicit weights are provided, the inverse of the error squared is used by default.
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

def std(x, dx, w=None, axis=None):

    # Use inverse of the errors squared for weights if not explictly provide
    if w is None:
        w = dx**(-2)

    mu, dmu = mean(x, dx, w=w, axis=axis)

    M = np.sum(w>0., axis=axis)
    sig = np.sqrt(np.nansum(w*(x-mu)**2, axis=axis)/((M-1)/M*np.nansum(w, axis=axis)))
    dsig = np.sqrt((np.nansum(w**2*(x-mu)**2*dx**2, axis=axis) + np.nansum(w*(x-mu), axis=axis)**2*dmu**2)/((M-1)/M*np.nansum(w, axis=axis)*np.nansum(w*(x-mu)**2, axis=axis)))

    return sig, dsig


def histogram(x, dx, w=None, bins=10, histrange=None):
    '''
    Bin data into a histogram accounting for error in the datapoints
    '''
    # Note - very basic, needs more work to match features of numpy.histogram
    from scipy.special import erf

    if w is None:
        w = dx**(-2)

    if not histrange:
        histrange = (np.nanmin(x), np.nanmax(x))

    bin_edges = np.linspace(histrange[0], histrange[1], bins+1)
    
    hist = np.zeros(bins)

    for m, s wi in zip(x, dx, w):

        edges_trans = (np.log(bin_edges) - m)/(s*np.sqrt(2))
        edges_erf = erf(edges_trans)

        hist += wi*np.diff(edges_erf)/2.

    return hist, bin_edges


