# Derivations

This documents contains the algebraic derivations of the error propigation formula used in this package in gory detail.  None of these are challenging to derive, but I could not find most of them conveniently listed anywhere reputable online, I will write them out here.

All derivations assume 
1. Input parameters are Gaussian random variables.
2. Input parameters are independent of each other (no coavariance).

Under such assumptions, the following generic formula are used to propogate error.  For function 

$$ f(x_1, x_2, ... x_N) $$

the standard error is given by

$$ \sigma_f = \sqrt{\sum_i^N \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_i^2} $$
