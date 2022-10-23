from re import X
from numpy.lib.function_base import average
import module

#========================================================

model = module.DialogElectra()
while True:
    x = input()
    y_hat = model.predict(x)
    print(y_hat)
