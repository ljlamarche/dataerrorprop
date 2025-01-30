# weighted.py
# Weighted versions of common data analysis functions that account for error propogation.
# If no explicit weights are provided, the inverse of the error squared is used by default.
# Functions take in both values and an equal sized array of their errors.
# All parameters are assumed to be Gaussian random variables.


import numpy as np

def _filter_finite(x, dx, w, axis=None):
    '''
    Mask any data points where either the data and/or the error is non-finite.
    '''

    finite_values = (np.isfinite(x) & np.isfinite(dx))
    N = np.sum(finite_values, axis=axis)
    fx = np.ma.masked_array(x, mask=~finite_values)
    fdx = np.ma.masked_array(dx, mask=~finite_values)
    fw = np.ma.masked_array(w, mask=~finite_values)

    return fx, fdx, fw, N


def mean(x, dx, w=None, axis=None):

    # Use inverse of the errors squared for weights if not explictly provide
    if w is None:
        w = dx**(-2)

    x, dx, w, N = _filter_finite(x, dx, w, axis=axis)

    mu = np.sum(w*x, axis=axis)/np.sum(w, axis=axis)
    dmu = np.sqrt(np.sum(w**2*dx**2, axis=axis))/np.sum(w, axis=axis)

    return mu, dmu

def std(x, dx, w=None, axis=None):

    # Use inverse of the errors squared for weights if not explictly provide
    if w is None:
        w = dx**(-2)

    x, dx, w, N = _filter_finite(x, dx, w, axis=axis)

    mu, dmu = mean(x, dx, w=w, axis=axis)

    M = np.sum(w>0., axis=axis)
    sig = np.sqrt(np.sum(w*(x-mu)**2, axis=axis)/((M-1)/M*np.sum(w, axis=axis)))
    dsig = np.sqrt((np.sum(w**2*(x-mu)**2*dx**2, axis=axis) + np.sum(w*(x-mu), axis=axis)**2*dmu**2)/((M-1)/M*np.sum(w, axis=axis)*np.sum(w*(x-mu)**2, axis=axis)))

    return sig, dsig


def histogram(x, dx, w=None, bins=10, histrange=None):
    '''
    Bin data into a histogram accounting for error in the datapoints
    '''
    # Note - very basic, needs more work to match features of numpy.histogram
    from scipy.special import erf

    if w is None:
        w = dx**(-2)

    x, dx, w, N = _filter_finite(x, dx, w)

    if not histrange:
        histrange = (np.min(x), np.max(x))

    bin_edges = np.linspace(histrange[0], histrange[1], bins+1)
    
    hist = np.zeros(bins)

    for m, s, wi in zip(x, dx, w):

        edges_trans = (bin_edges - m)/(s*np.sqrt(2))
        edges_erf = erf(edges_trans)

        hist += wi*np.diff(edges_erf)/2.

    return hist, bin_edges


