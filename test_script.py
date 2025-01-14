import dataerrorprop.standard as ep
import numpy as np

rng = np.random.default_rng()
x = rng.normal(10, 0.1, 1000)
s = rng.normal(0, 0.1, 1000)
# s = np.abs(x-10)

mu, dmu = ep.mean(x, s)
print(mu, dmu)

sig, dsig = ep.stddev(x, s)
print(sig, dsig)

hist, be = ep.histogram(x, s)
print(hist, be)
