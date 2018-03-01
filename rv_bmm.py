import numpy as np
import scipy.stats as stat
from itertools import chain

def rvs_bmm(parameter_beta, mixture_rate, sample_size, seed = None):

    if seed is None:
        seed = 0
    else:
        pass

    try:
        if all([len(parameter_beta[i]) == 2 for i in range(len(parameter_beta))]):
            pass
        else:
            raise ValueError('each beta distribution must have 2 parameters')

        if len(parameter_beta) == len(mixture_rate):
            pass
        else:
            raise ValueError('number of beta distributions and mixture rates must be equaled')

        if all([all([parameter_beta[i][0]>0, parameter_beta[i][1]>0]) for i in range(len(parameter_beta))]):
            pass
        else:
            raise ValueError("each beta distribution's parameter must be positive value")

    except TypeError:
        print('each beta distribution must have 2 parameters')

    m = stat.multinomial.rvs(sample_size, mixture_rate)
    rvs = [list(stat.beta.rvs(i[0], i[1], size=j)) for i, j in zip(parameter_beta, m)]
    rv = np.array(list(chain.from_iterable(rvs))).reshape((sample_size, 1))

    return rv

parameter_beta = ((1,3),(3,1),(0.5,0.5))
mixture_rate = (0.2, 0.5, 0.3)
sample_size = 100
rv = rvs_bmm(parameter_beta, mixture_rate, sample_size)
print(type(rv), rv.shape, rv)
