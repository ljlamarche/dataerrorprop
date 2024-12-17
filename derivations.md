# Derivations

This documents contains the algebraic derivations of the error propigation formula used in this package in gory detail.  None of these are challenging to derive, but I could not find most of them conveniently listed anywhere reputable online, I will write them out here.

All derivations assume 
1. Input parameters are Gaussian random variables.
2. Input parameters are independent of each other (no coavariance).

Under such assumptions, the following generic formula are used to propogate error.  For function 

$$ f(x_1, x_2, ... x_N) $$

the standard error is given by

$$ \sigma_f = \sqrt{\sum_i^N \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_i^2} $$

## Mean

$$ \mu = \frac{\sum_i^N x_i}{N} $$

$$ \frac{\partial \mu}{\partial x_i} = \frac{1}{N} $$

$$ \sigma = \sqrt{\sum_i^N \left(\frac{\partial \mu}{\partial x_i}\right)^2 \sigma_i^2} $$

$$ \sigma = \sqrt{\sum_i^N \left(\frac{1}{N}\right)^2 \sigma_i^2} = \sqrt{\sum_i^N \frac{\sum_i^N \sigma_i^2}{N}} $$

## Error-Weighted Mean
Each value is weighted by the inverse of its error squared such that points with greater error contribute less to the resulting mean.

$$ \mu = \frac{\sum_i^N \frac{x_i}{\sigma_i^2}}{\sum_i^N \frac{1}{\sigma_i^2}} = \frac{1}{\sum_i^N \sigma_i^{-2}}\sum_i^N \frac{x_i}{\sigma_i^2} $$

$$ \frac{\partial \mu}{\partial x_i} = \frac{1}{\sum_i^N \sigma_i^{-2}} \left(\frac{1}{\sigma_i^2}\right)  = \frac{\sigma_i^{-2}}{\sum_i^N \sigma_i^{-2}} $$

$$ \sigma = \sqrt{\sum_i^N \left(\frac{\partial \mu}{\partial x_i}\right)^2 \sigma_i^2} $$

$$ \sigma = \sqrt{\sum_i^N \left(\frac{\sigma_i^{-2}}{\sum_i^N \sigma_i^{-2}}\right)^2 \sigma_i^2} $$

$$ \sigma = \sqrt{\sum_i^N \frac{\sigma_i^{-4}}{\left(\sum_i^N \sigma_i^{-2}\right)^2}\sigma_i^2} = \sqrt{\sum_i^N \frac{\sigma_i^{-2}}}{\left(\sum_i^N \sigma_i^{-2}\right)^2} $$

$$ \sigma = \sqrt{\frac{1}{\left(\sum_i^N \sigma_i^{-2}\right)^2} \left(\sum_i^N \sigma_i^{-2}\right)} = \sqrt{\frac{1}{\sum_i^N \sigma_i^{-2}}} $$
