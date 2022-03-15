import scipy as sp
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import sys
import os

eval1 = sys.argv[1]
eval2 = sys.argv[2]

comp1, comp2 = [], []
with open(eval1, 'r') as f:
    for line in f.readlines():
        comp1.append(int(line.strip()))

with open(eval2, 'r') as f:
    for line in f.readlines():
        comp2.append(int(line.strip()))

tau, p_val = sp.stats.kendalltau(comp1, comp2)

print(tau.round(4))
print((1+tau.round(4))*50)
