import numpy as np
import scipy.stats as stat
from itertools import chain

def rvs_bmm(a, b, n, p):
    
    m = stat.multinomial.rvs(n, p)
    rvs = [list(stat.beta.rvs(i, j, size=k)) for i, j, k in zip(a, b, m)]
    rv = np.array(list(chain.from_iterable(rvs))).reshape((n,1))

    return rv

# a = np.array([1, 3, 0.5])
# b = np.array([3, 1, 0.5])
# n = 100
# p = np.array([0.3, 0.6, 0.1])

# rv = rvs_bmm(a, b, n, p)
# print(type(rv), rv.shape, rv)
