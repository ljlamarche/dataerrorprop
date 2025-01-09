# dataerrorprop

This package offers versions of common data analysis and statistics functions that account for errors/uncertainty in the data.  It is designed to provide functions that can be used as drop-in replacements for some common numpy functions.

The actual equations used for these calculations are available in the `derivations.md` file in the root of this repository.

## Installation
This package can be installed with pip from GitHub.
```
$ pip install git+https://github.com/ljlamarche/dataerrorprop.git
```

## Usage
This package provides two modules: `standard` is the normal functions with the resulting error calculated while `weighted` allows for each point to be assigned an indepdendent weight.  If no weights are provided, the inverse of the error squared is used as weights.

### Standard Module Example

```
import dataerrorprop.standard as dep
import numpy as np

rng = np.random.default_rng()
x = rng.normal(10, 0.1, 1000)
dx = rng.normal(0, 0.1, 1000)

avg, avg_err = dep.mean(x, dx)
print(avg, avg_err)

std, std_err = ep.std(x, dx)
print(std, std_err)
```

### Weighted Module Example

```
import dataerrorprop.weighted as dep
import numpy as np

rng = np.random.default_rng()
x = rng.normal(10, 0.1, 1000)
dx = rng.normal(0, 0.1, 1000)

avg, avg_err = dep.mean(x, dx)
print(avg, avg_err)

std, std_err = ep.std(x, dx)
print(std, std_err)
```

## Contributions

Contributions and additions to this package are welcome!  If you find an error or a bug, or have a new standard function you think it would be useful to have error propigation for, please open an issue or submit a PR.
