import numpy as np
from collections import Counter
import time
import math


data = [1,2,3,4,5]
 

def add_x(data,x):
    for i in range(len(data)):
        data[i] = data[i]*x
    return data

modified = add_x(data,4)
print(modified)

#matrixes and functions to replace numpy (not in use, but if I figure out how to turn the nested list i generate into a tuple of integers, I will implement so I can remove numpy. For now it is used for np.zeros.)
def fakenpzeros(size): #Creates a nested list that looks exactly like a matrix np.zeros() would produce. HOWEVER it is not a tupe of integers so I cannot use for mathematical operations YET
    rows, cols = 1, size
    matrix = [([0]*cols) for i in range(rows)]
    return matrix[0]
def fakenpsum(m):
    return sum(sum(i) for i in m) #Deprecated but was going to use as replacement for np.sum()
def fakenpsumcol(m, c):
    return sum(i[c] for i in m) #Also deprecated, same as above but for columns, deprecated since matrixes I require only are one dimensional.


#Pseudo random number stuff
def pseudo_uniform_bad(mult=5,
                       mod=11,
                       seed=1,
                       size=1):
    """
    Generates a 'random' number that is set by modules and multipliers (not good)
    """
    U = np.zeros(size)
    x = (seed*mult+1)%mod
    U[0] = x/mod
    for i in range(1,size):
        x = (x*mult+1)%mod
        U[i] = x/mod
    return(U)
def pseudo_uniform_good(mult=16807,
                        mod=(2**31)-1,
                        seed=123456789,
                        size=1):
    """
    Generates a reasonable and random number
    """
    U = fakenpzeros(size)
    print(U)
    x = (seed*mult+1)%mod
    U[0] = x/mod
    for i in range(1,size):
        x = (x*mult+1)%mod
        U[i] = x/mod
        print(U[i])
    return(U)
def pseudo_uniform(low=0,
                   high=1,
                  seed=123456789,
                  size=1):
    """
    Makes a decently random number between the set limits
    """
    return(low+(high-low)*pseudo_uniform_good(seed=seed,size=size))
def sample_pick(lst, k):
    l2 = [] #creates a list to be used for storing the samples
    """
    Picks up a random sample from a given list
    """
    # Sets seed based on the decimal portion of the current system clock
    for i in range(k): #repeats this code k number of time
        t = time.perf_counter() #gets the time
        seed = int(10**9*float(str(t-int(t))[0:])) #multipilies the time by 10^9 as a float and takes it away from an integerized time, guarantees a decimal number.
        # Random sample as an index
        l = len(lst)
        s = pseudo_uniform(low=0,high=l,seed=seed,size=1)
        idx = int(s)
        l2.append((lst[idx])) #SAMPLING
    return(l2)

#USELESS/FULLY DEPRECATED
#Used for graphing or extension if needed
def pseudo_bernoulli(p=0.5,size=1):
    """
    Bernoulli generator from uniform generator
    """
    # Sets seed based on the decimal portion of the current system clock
    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    B = pseudo_uniform(seed=seed,size=size)
    B = (B<=p).astype(int)
    
    return B #useless
def pseudo_binomial(n=100,
                   p=0.5,
                   size=1):
    """
    Binomial distribution from the Uniform generator
    """
    binom = []
    for _ in range(size):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudo_uniform(size=n,seed=seed)
        Y = (U <= p).astype(int)
        binom.append(np.sum(Y))
    
    return binom #useless
def pseudo_normal(mu=0.0,sigma=1.0,size=1):
    """
    Generates Normal distribution from the Uniform distribution using Box-Muller transform
    """
    # A pair of Uniform distributions
    t = time.perf_counter()
    seed1 = int(10**9*float(str(t-int(t))[0:]))
    U1 = pseudo_uniform(seed=seed1,size=size)
    t = time.perf_counter()
    seed2 = int(10**9*float(str(t-int(t))[0:]))
    U2 = pseudo_uniform(seed=seed2,size=size)
    # Standard Normal pair
    Z0 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    Z1 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)
    # Scaling
    Z0 = Z0*sigma+mu
    
    return Z0 #useless
def pseudo_exp(lamb,size=1):
    """
    Generates exponential distribution from the Uniform distribution
    """
    t = time.perf_counter()
    seed = int(10**9*float(str(t-int(t))[0:]))
    U = pseudo_uniform(size=size,seed=seed)
    X = -(1/lamb)*(np.log(1-U))
    
    return X #useless
def pseudo_poisson(alpha,size=1):
    """
    """
    poisson = []
    for _ in range(size):
        t = time.perf_counter()
        seed = int(10**9*float(str(t-int(t))[0:]))
        U = pseudo_uniform(seed=seed,size=5*alpha)
        X,P,i = 0,1,0
        while P >= np.exp(-alpha):
            P = U[i]*P
            X+=1
            i+=1
        poisson.append(X)
    return np.array(poisson) #useless