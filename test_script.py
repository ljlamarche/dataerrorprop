import dataerrorprop.errorweight as ep
import numpy as np

rng = np.random.default_rng()
x = rng.normal(10, 0.1, 1000)
s = rng.normal(0, 0.1, 1000)

mu, sig = ep.mean(x, s)
print(mu, sig)
