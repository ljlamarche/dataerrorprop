import dataerrorprop.weighted as ep
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

print(ep.mean(x_1d_nan, dx_1d_nan))

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


#rng = np.random.default_rng()
#x = rng.normal(3, 5., (4,4))
#s = rng.normal(0, 1., (4,4))
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
