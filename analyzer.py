import numpy as np

def calculate_mean(data, column):
    return np.mean(data[:,column], axis=0)

def calculate_median(data, column):
    return np.median(data[:,column], axis=0)

def calculate_std(data, column):
    return np.std(data[:,column], axis=0)