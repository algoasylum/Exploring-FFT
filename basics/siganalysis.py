import numpy as np

def norm_1(sig):
    return np.abs(sig).sum()

def norm_2(sig):
    return np.sqrt(np.square(sig).sum())

def norm_infty(sig):
    return np.max(sig)
