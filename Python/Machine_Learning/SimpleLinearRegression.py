from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs=np.array([1,2,3,4,5,6],dtype=np.float64)
ys=np.array([5,4,6,5,6,7],dtype=np.float64)

def bestfitslopeandintercept(xs,ys):
    m=(((mean(xs)*mean(ys))-mean(xs*ys))/ 
       (mean(xs)**2 - mean(xs**2))
       )
    b=mean(ys)-m*mean(xs)
    return m,b


def squaredError(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2)

def coeffOfDetermination(ys_orig,ys_line):
    y_mean_line=[mean(ys_orig) for y in ys_orig]
    squaredErrorReg = squaredError(ys_orig, ys_line)
    squaredErrorYMean = squaredError(ys_orig, y_mean_line)
    return 1 - (squaredErrorReg/squaredErrorYMean)

m,b=bestfitslopeandintercept(xs,ys)

print(m,b)
regression_line=[(m*x)+b for x in xs]

r_squared= coeffOfDetermination(ys, regression_line)

print(r_squared)

plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()







