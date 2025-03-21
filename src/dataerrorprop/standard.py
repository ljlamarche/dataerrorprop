# standard.py
# Common data analysis functions with error propigation.
# Functions take in both values and an equal sized array of their errors.
# All parameters are assumed to be Gaussian random variables.


import numpy as np


def _filter_finite(x, dx, axis=None):
    '''
    Mask any data points where either the data and/or the error is non-finite.
    '''

    finite_values = (np.isfinite(x) & np.isfinite(dx))
    N = np.sum(finite_values, axis=axis)
    fx = np.ma.masked_array(x, mask=~finite_values)
    fdx = np.ma.masked_array(dx, mask=~finite_values)

    return fx, fdx, N


def mean(x, dx, axis=None):
    '''
    Calculate the average and the error on the average.
    '''

    x, dx, N = _filter_finite(x, dx, axis=axis)

    mu = np.sum(x, axis=axis)/N
    dmu = np.sqrt(np.sum(dx**2, axis=axis))/N

    return mu, dmu


def std(x, dx, axis=None):
    '''
    Calculate the standard deviation and the error on the standard deviation.
    '''

    x, dx, N = _filter_finite(x, dx, axis=axis)

    mu, dmu = mean(x, dx, axis=axis)
    sig = np.sqrt(np.sum((x-mu)**2/(N-1), axis=axis))
    dsig = np.sqrt((np.sum((x-mu)**2*dx**2, axis=axis) + np.sum(x-mu, axis=axis)**2*dmu**2)/((N-1)*np.sum((x-mu)**2, axis=axis)))

    return sig, dsig


def histogram(x, dx, bins=10, histrange=None):
    '''
    Bin data into a histogram accounting for error in the datapoints
    '''
    # Note - very basic, needs more work to match features of numpy.histogram
    from scipy.special import erf

    x, dx, N = _filter_finite(x, dx)

    if not histrange:
        histrange = (np.min(x), np.max(x))

    bin_edges = np.linspace(histrange[0], histrange[1], bins+1)
    
    hist = np.zeros(bins)

    for m, s in zip(x, dx):

        edges_trans = (bin_edges - m)/(s*np.sqrt(2))
        edges_erf = erf(edges_trans)

        hist += np.diff(edges_erf)/2.

    return hist, bin_edges


