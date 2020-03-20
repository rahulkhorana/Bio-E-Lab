"""
Bio-E Lab ITU

Dr. John Ladasky
Rahul Khorana
"""
#program starts here
import scipy
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


with open('2018-07-02 and 07-09.xlsx - Sheet2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(type(row), [type(item) for item in row])
        print(', '.join(row))
        
def func(x, a, b, c):
    return a * np.exp(-b * x) +c

# Generate some data, a curve of the type described in func()
# with the coefficients known and some added noise.
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise

# Plot the raw data.
plt.scatter(xdata, ydata)

# Fit the curve.
coefficients, unused = curve_fit(func, xdata, ydata)
print(coefficients)

# Plot the fitted curve.
yfit = func(xdata, *coefficients)
plt.plot(xdata, yfit)



plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
