import matplotlib
 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd

def NN(m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1 + np.exp(-x))


def cost(b):
    return (b-4) ** 2


w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()





