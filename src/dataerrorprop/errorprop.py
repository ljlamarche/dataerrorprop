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


def stddev(x, dx, axis=None):
    '''
    Calculate the standard deviation and the error on the standard deviation.
    '''

    N = np.sum(np.isfinite(x), axis=axis)
    mu, dmu = mean(x, dx)

    sig = np.sqrt(np.nansum((x-mu)**2)/(N-1))
    dsig = np.sqrt((np.nansum((x-mu)**2*dx*2) + np.nansum(x-mu)**2*dmu**2)/((N-1)*np.nansum((x-mu)**2)))

    return sig, dsig


def histogram(x, dx, bins=10, histrange=None):
    '''
    Bin data into a histogram accounting for error in the datapoints
    '''
    # Note - very basic, needs more work to match features of numpy.histogram
    from scipy.special import erf

    if not histrange:
        histrange = (np.nanmin(x), np.nanmax(x))

    bin_edges = np.linspace(histrange[0], histrange[1], bins+1)
    
    hist = np.zeros(bins)

    for m, s in zip(x, dx):

        edges_trans = (np.log(bin_edges) - m)/(s*np.sqrt(2))
        edges_erf = erf(edges_trans)

        hist += np.diff(edges_erf)/2.

    return hist, bin_edges


