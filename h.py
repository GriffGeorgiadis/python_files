def points(n):
    # Make points by squaring x
    # where x is random in (0,1)
    Y = []
    for i in range(n):
        x = random()
        Y.append(x*x)
    return Y

Y = points(10000) # Make a load of points
from pylab import *
figure()
hist(Y, 100) # The second argument is the number of bins
show()
