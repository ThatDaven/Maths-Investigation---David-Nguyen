import math as math
import random
from collections import Counter

x = []

def minimum(x):
  x.sort()
  min = x[0]
  return float(min)
def maximum(x):
  x.sort()
  max = x[-1]
  return float(max)
def range_lst(x):
  return float(max(x)) - float(min(x))
def total(x):
  """Get the sum of a list of numbers."""
  total = 0 # start with zero
  for i in x: # iterate over each value in the list
    total += i  # add val to the running total
  return float(total)
def mean(x):
  n = len(x) #assigns a variable the value of how many numbers there are in the list
  summ = total(x) #adds up all the numbers within the list
  mo = summ / n #divides the total sum by the number of numbers (just like how you would obtain the average)
  return(f"The mean/average for all of these numbers is {round(mo, 3)}") #MEAN
def mode(x):
  count = Counter(x)
  m = [_ for _, i in count.items() if i == count.most_common(1)[0][1]]
  return m
def median(x):
  no = len(x) #finds out how many numbers there are
  x.sort() #sorts the list from lowest to highest incase it was inputted randomly
  if no % 2 == 0: #if the list's number is not divisible by 2 (meaning it has a non stated median)
      me1 = x[no // 2] #finds the middle number
      me2 = x[no // 2 - 1] #finds the number before that
      me = (me1 + me2) / 2 #finds the number between both of those numbers
  else:
      me = x[no // 2] #divide the list into 2 to find the middle number x[0] 0 is the number/placement of the number, so no // 2 in a list of 11 numbers would point to the 6th number. x[no //2] = x[11 // 2]
  return me #MEDIAN
def variance(x):
  mean = total(x) / len(x) #same as above
  var = total((l - mean)**2 for l in x) / len(x) #same as above
  return var #Find the variance, quite literally just the code above but without using square-root
def stand_dev(x):
  h = math.sqrt(variance(x)) #gets variance and square roots to get std
  return h
def lower_quartile(x):
  x = sorted(x) #sorts list
  middle = len(x) // 2 #gets the middle of the list
  return median(x[:middle]) #returns middle of the middle of the list (half of half is 1/4)
def upper_quartile(x):
  x = sorted(x) #same
  middle = len(x) // 2 #same
  if len(x) % 2 == 0: #if length is divisible by 2
      return median((x[middle:])) #get perfect middle
  else:
      return median((x[middle + 1:])) #get middle between 2 middles
def fn_summary(x): #calls all the fucntions needed
  return f"The minimum is: {minimum(x)}, The lower quartile is: {lower_quartile(x)}, The median is: {median(x)}, The upper quartile is: {upper_quartile(x)}, The maximum is: {maximum(x)}"
def inter_qr(x):
  u = upper_quartile(x) #get
  l = lower_quartile(x) #get
  return u - l #get range between
################################################################################################################################## 
def sample_pick_replacement(x, num): #gets random sample without repetitions by using randint and getting numbers from the randomth place in a list
  if num > len(x):
    return "Sample size is larger than list"
  else:
    h = []
    for i in range(num):
        n = random.randint(0, len(x) - 1)
        h.append(x[n])
        x.pop(n)
    return h
