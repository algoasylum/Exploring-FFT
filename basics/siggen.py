import numpy as np

def gen_sig_delta(length, n):
    signal_d = np.zeros(length)
    if n >= 0 & n < length:
        signal_d[n] = 1
    return signal_d

def gen_sig_unit_step(length, n):
    signal_us = np.zeros(length)
    if n >= 0 & n < length:
        signal_us[n:] = 1
    return signal_us

def gen_sig_unit_pulse(length, n_1, n_2):
    signal_us = np.zeros(length)
    if n_1 > n_2:
        n_1, n_2 = n_2, n_1
    if n_1 >= 0 & n_2+1 < length:
        signal_us[n_1:n_2+1] = 1
    return signal_us

def gen_sig_sin(length, n, N):
    signal_sin = np.zeros(length)
    omega = 2 * np.pi * n / N
    for k in range(length):
        signal_sin[k] = np.sin(omega * k)
    return signal_sin

def gen_sig_cos(length, k, N):
    signal_cos = np.zeros(length)
    omega = 2 * np.pi * k / N
    for n in range(length):
        signal_cos[n] = np.cos(omega * n)
    return signal_cos

def gen_sig_cos2(length, k, N):
    omega = 2 * np.pi * k / N
    return [np.cos(omega * n) for n in range(length)]
