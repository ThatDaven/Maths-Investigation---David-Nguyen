import numpy as np
from collections import Counter
import time
import math

#Number generator using your clock
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
    U = np.zeros(size)
    x = (seed*mult+1)%mod
    U[0] = x/mod
    for i in range(1,size):
        x = (x*mult+1)%mod
        U[i] = x/mod
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
