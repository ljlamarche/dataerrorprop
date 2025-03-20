import dataerrorprop.standard as ep
import numpy as np
import pytest

# Tests
# All functions
# Flat arrays
# 2D arrays
# Do computation along specific axis (not implimented)
# Nans included
# Infs included

x_1d = np.array([6.76,  -0.37,  8.05,  4.56,  0.82,  7.24, 1.12,  0.21, -7.73,  1.56])
dx_1d = np.array([0.84,  0.36, -0.35,  0.15, -0.29,  0.12, -1.37, -1.56,  0.16,  0.43])
x_1d_nan = np.array([6.76,  -0.37,  np.nan,  4.56,  0.82,  np.nan, 1.12,  0.21, -7.73,  1.56])
dx_1d_nan = np.array([0.84,  0.36, -0.35,  0.15, -0.29,  0.12, -1.37, -1.56,  np.nan,  0.43])
x_2d = np.array([[ 0.42,  3.87,  0.73,  9.99],
                 [ 1.57,  0.33,  2.47,  0.30],
                 [ 1.53, -0.22,  4.20, -0.08]])
dx_2d = np.array([[-0.76, -0.96, -0.68,  0.58],
                  [ 1.32,  1.44, -1.07, -0.96],
                  [-1.08, -0.49, -1.15, -0.17]])
x_2d_nan = np.array([[ 0.42,  3.87,  0.73,  9.99],
                     [ np.nan,  0.33,  2.47,  0.30],
                     [ 1.53, -0.22,  np.nan, -0.08]])
dx_2d_nan = np.array([[-0.76, np.nan, -0.68,  0.58],
                      [ 1.32,  1.44, -1.07, -0.96],
                      [-1.08, -0.49, np.nan, -0.17]])



#@pytest.mark.parametrize('x', [x_1d, x_1d_nan])
#@pytest.mark.parametrize('dx', [dx_1d, dx_1d_nan])

#print(ep.mean(np.array([1.,2.]), np.array([0.5, 0.1]), w=np.array([1,5])))

# Check functions returning correct numeric values for known test numbers
@pytest.mark.parametrize('x,dx,expected', [(x_1d,dx_1d,(2.222, 0.236637)), (x_2d, dx_2d, (2.0925 , 0.27561))])
def test_mean(x, dx, expected):
    out = ep.mean(x, dx)
    np.testing.assert_allclose(out, expected, rtol=1e-4)


@pytest.mark.parametrize('x,dx', [(x_1d_nan, dx_1d_nan), (x_2d_nan, dx_2d_nan)])
def test_mean_nan(x, dx):
    
    # Remove NaNs from input arrays
    finite_values = (np.isfinite(x) & np.isfinite(dx))
    x_rm_nan = x[finite_values]
    dx_rm_nan = dx[finite_values]
    expected = ep.mean(x_rm_nan, dx_rm_nan)

    out = ep.mean(x, dx)
    np.testing.assert_allclose(out, expected, rtol=1e-4)

@pytest.mark.parametrize('axis', [0,1])
@pytest.mark.parametrize('x,dx', [(x_2d, dx_2d), (x_2d_nan, dx_2d_nan)])
def test_mean_axis(x, dx, axis):

    mu, dmu = ep.mean(x, dx, axis=axis)
    expected = tuple(s for i, s in enumerate(x.shape) if i != axis)
    np.testing.assert_equal(mu.shape, expected)
    np.testing.assert_equal(dmu.shape, expected)



@pytest.mark.parametrize('x,dx,expected', [(x_1d,dx_1d,(4.697904, 0.139843)), (x_2d, dx_2d, (2.887969, 0.208976))])
def test_std(x, dx, expected):
    out = ep.std(x, dx)
    np.testing.assert_allclose(out, expected, rtol=1e-4)


@pytest.mark.parametrize('x,dx', [(x_1d_nan, dx_1d_nan), (x_2d_nan, dx_2d_nan)])
def test_std_nan(x, dx):
    
    # Remove NaNs from input arrays
    finite_values = (np.isfinite(x) & np.isfinite(dx))
    x_rm_nan = x[finite_values]
    dx_rm_nan = dx[finite_values]
    expected = ep.mean(x_rm_nan, dx_rm_nan)

    out = ep.mean(x, dx)
    np.testing.assert_allclose(out, expected, rtol=1e-4)

@pytest.mark.parametrize('axis', [0,1])
@pytest.mark.parametrize('x,dx', [(x_2d, dx_2d), (x_2d_nan, dx_2d_nan)])
def test_std_axis(x, dx, axis):

    mu, dmu = ep.mean(x, dx, axis=axis)
    expected = tuple(s for i, s in enumerate(x.shape) if i != axis)
    np.testing.assert_equal(mu.shape, expected)
    np.testing.assert_equal(dmu.shape, expected)

#@pytest.mark.parametrize('x', [x_1d, x_1d_nan])
#@pytest.mark.parametrize('dx', [dx_1d, dx_1d_nan])
#def test_std(x, dx):
#    out = ep.std(x, dx)
#    np.testing.assert_allclose(out, (4.697904, 0.139843), rtol=1e-4)

# Check functions return real values when NaNs included in array

# Check that a multidimentional array returns a single value if no axes are specified


# Check that a multidimensional array returns a sliced array if axes are specified




# The following tests are more statistical in nature and desined to check that the
#   functions do what they are mathematically expected to do rather than that they 
#   just are returning consistent results.  Many use randomly generated arrays and
#   may occasionally fail.  If so, try rerunning the test.  If a test is consistently
#   failing, the actual function may not be implimented correctly or the derivation
#   may not be correct.


# Check that standard mean/std are the same as that calculated with numpy functions regardless of provided errors
def test_mean_numpy():

    rng = np.random.default_rng()
    x = rng.normal(3., 5., 100)
    s = rng.normal(0, 0.5, 100)

    ep_mean, _ = ep.mean(x, s)
    np_mean = np.mean(x)

    np.testing.assert_allclose(ep_mean, np_mean)


def test_std_numpy():

    rng = np.random.default_rng()
    x = rng.normal(3., 5., 100)
    s = rng.normal(0, 0.5, 100)

    ep_std, _ = ep.std(x, s)
    np_std = np.std(x, ddof=1)

    np.testing.assert_allclose(ep_std, np_std)


# Following two tests are mathematically satesfying to confirm, but probably not strictly
#   necessary checks of the code, especially if the prior two checks against numpy pass

# Check that calculated mean is within the standard error (https://en.wikipedia.org/wiki/Standard_error)
def test_mean_standard_error():

    rng = np.random.default_rng()

    N = 100
    mu = 3.
    sig = 5.

    # Calculate standard error
    std_err = sig/np.sqrt(N)

    one_sigma = 0
    N_redraw = 10000
    for _ in range(N_redraw):
        # Generate redraw arrays
        x = rng.normal(mu, sig, N)
        s = rng.normal(0, 0.5, N)
        # Calculate mean of redraw 
        ep_mean, _ = ep.mean(x, s)
        # Check if redraw mean within standard error of true mean
        if np.abs(ep_mean-mu)<=std_err:
            # Tally if redraw within one sigma
            one_sigma += 1

    # Check that the percentage of redraws within one sigma match the standard one sigma percentage (68.2%)
    np.testing.assert_allclose(one_sigma/N_redraw, 0.682, rtol=0.05)


# Check that calculated standard deviation is within the standard error (https://web.eecs.umich.edu/~fessler/papers/files/tr/stderr.pdf)
def test_std_standard_error():

    rng = np.random.default_rng()

    N = 100
    mu = 3.
    sig = 5.

    # Calculate standard error
    std_err = sig/np.sqrt(2*(N-1))

    one_sigma = 0
    N_redraw = 10000
    for _ in range(N_redraw):
        # Generate redraw arrays
        x = rng.normal(mu, sig, N)
        s = rng.normal(0, 0.5, N)
        # Calculate standard deviation of redraw 
        ep_std, _ = ep.std(x, s)
        # Check if redraw standard deviation within standard error of true standard deviation
        if np.abs(ep_std-sig)<=std_err:
            # Tally if redraw within one sigma
            one_sigma += 1

    # Check that the percentage of redraws within one sigma match the standard one sigma percentage (68.2%)
    np.testing.assert_allclose(one_sigma/N_redraw, 0.682, rtol=0.05)


## Some Monte Carlo stuff to demonstrate propogated error is correct?
def test_mean_error_onesig():

    rng = np.random.default_rng()
    x = rng.normal(3., 5., 100)
    s = np.abs(rng.normal(0, 0.5, 100))

    # Calculate mean and error on mean
    ep_mean, ep_err = ep.mean(x, s)

    one_sigma = 0
    N_redraw = 10000
    for _ in range(N_redraw):
        # Generate redraw array
        x_redraw = [rng.normal(x1, s1, 1) for x1, s1 in zip(x, s)]
        # Check if redraw mean within calculated error on mean
        if np.abs(ep_mean-np.mean(x_redraw))<=ep_err:
            # Tally if redraw mean within one sigma 
            one_sigma += 1

    # Check that the percentage of redraws within one sigma match the standard one sigma percentage (68.2%)
    np.testing.assert_allclose(one_sigma/N_redraw, 0.682, rtol=0.05)


#def test_std_error_onesig():
#    # This routinely fails
#    # Standard Deviation is a positive definite value, so the standard one sigma values don't apply?
#    # Test needs some kind of revisions
#
#    rng = np.random.default_rng()
#    x = rng.normal(3., 5., 100)
#    s = np.abs(rng.normal(0, 0.5, 100))
#
#    # Calculate mean and error on mean
#    ep_std, ep_err = ep.std(x, s)
#
#    one_sigma = 0
#    N_redraw = 10000
#    for _ in range(N_redraw):
#        # Generate redraw array
#        x_redraw = [rng.normal(x1, s1, 1) for x1, s1 in zip(x, s)]
#        # Check if redraw mean within calculated error on mean
#        if np.abs(ep_std-np.std(x_redraw, ddof=1))<=ep_err:
#            # Tally if redraw mean within one sigma 
#            one_sigma += 1
#
#    # Check that the percentage of redraws within one sigma match the standard one sigma percentage (68.2%)
#    np.testing.assert_allclose(one_sigma/N_redraw, 0.682, rtol=0.05)


#1. Get random array of values and errors
#2. Calculate mean and error for array
#3. For each element in the array, redraw from a distrubution where the value is the mean and the error is the standard deviation.
#4. Calculate the mean of the redrawn distribution.
#5. Repete steps 3-4 a large number of times.
#6. Check to see that the means of the redraw distribution are within the error estimate of the primary distribution


#rng = np.random.default_rng()
#x = rng.normal(3, 5., 10000)
#s = rng.normal(0, 0.1, 10000)
#
##for mu in [1., 2.]:
#
#
#print(np.mean(x), np.std(x))
#print(ep.mean(x, s), ep.std(x, s))
#
#def gaussian(x, mu, sig):
#    return np.exp(-(x-mu)**2/(2*sig**2))/(np.sqrt(np.pi)*sig)
#
#import matplotlib.pyplot as plt
#plt.hist(x, bins=50, density=True)
#xg = np.arange(-10., 25., 0.1)
#plt.plot(xg, gaussian(xg, 3., 5.))
#plt.show()


#print(x, s)
## s = np.abs(x-10)
#
#mu, dmu = ep.mean(x, s)
#print(mu, dmu)
#
#sig, dsig = ep.stddev(x, s)
#print(sig, dsig)
#
#hist, be = ep.histogram(x, s)
#print(hist, be)
