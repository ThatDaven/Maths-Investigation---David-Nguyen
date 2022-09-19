import math
from collections import Counter
from lazy_functions import *
import math

def mode(x):
    count = Counter(x) #Counts the numbers in the list
    m = [k for k, i in count.items() if i == count.most_common(1)[0][1]] #runs through the whole list and counts the number that repeats the most by continuously looping through and comparing the list to one that has removed numbers until it finds number/s that repeat the most.
    return(f"The mode/s of these numbers is/are: {m}.") #MODE
def mean(x):
    n = len(x) #assigns a variable the value of how many numbers there are in the list
    summ = sum(x) #adds up all the numbers within the list
    mo = summ / n #divides the total sum by the number of numbers (just like how you would obtain the average)
    return(f"The mean/average for all of these numbers is {round(mo, 3)}") #MEAN
def median(x):
    no = len(x) #finds out how many numbers there are
    x.sort() #sorts the list from lowest to highest incase it was inputted randomly
    if no % 2 == 0: #if the list's number is not divisible by 2 (meaning it has a non stated median)
        me1 = x[no // 2] #finds the middle number
        me2 = x[no // 2 - 1] #finds the number before that
        me = (me1 + me2) / 2 #finds the number between both of those numbers
    else:
        me = x[no // 2] #divide the list into 2 to find the middle number x[0] 0 is the number/placement of the number, so no // 2 in a list of 11 numbers would point to the 6th number. x[no //2] = x[11 // 2]
    return(f"The median of all these numbers is {me}") #MEDIAN
def sort(x):
    n = sorted(x)
    return(n) #SORT - Useless
def score(x):
    n = len(x)
    return(F'The number of values within this list is {n}') #SCORE
def std(x):
    #return("List : " + str(x))
    mean = sum(x) / len(x)  #finds our mean, using code above
    var = sum((l - mean)**2 for l in x) / len(x) #finds the variance by squaring all the numbers in the list - the mean before dividing by the numbers of numbers in the list (formular of variance is that)
    st_dev = math.sqrt(var) #square roots the result to get the standard deviation
    return("Standard deviation of the given list: " + str(st_dev)) #Find the standard deviation
def var(x):
    #return("List : " + str(x))
    mean = sum(x) / len(x) #same as above
    var = sum((l - mean)**2 for l in x) / len(x) #same as above
    return("Variance of the given list: " + str(var)) #Find the variance, quite literally just the code above but without using square-root
def revsort(x):
    n = sorted(x, reverse=True)
    return(n) #REVERSE SORT - Useless
def range(x):
    n = max(x) - min(x) #takes the lowest number and the largest number and subtracts the lowest from the largest to find the range
    return(n) #Find the range
def quartile(x):
    length = len(x)  #finds how many numbers in the list
    start = (length)//2 #finds the median (doesn't apply checks properly for even numbered list here but that is checked later)
    if length%2: #checks if the length of list is divisble by 2
        start = start #keeps the start the same if so
        end = start + 1 #sets our ending point for calculcation according to checks
        median = sum(x[start:end]) #sum single element list as value
    else:
        start = start - 1 #if list is not divisible by 2 evenly, move the start back by 1
        end = start + 2 #basically the end is still the same
        median = sum(x[start:end]) / 2.  #Average middle two elements
    #1st quartile
    q1start = start//2
    flag = False
    if start%2:
        q1start = q1start
        q1end = q1start + 1
        q1 = sum(x[q1start:q1end]) # a single element
    else:
        flag = True
        q1start = q1start - 1
        q1end = q1start + 2
        q1 = sum(x[q1start:q1end]) / 2. # Average middle two elements
    #3rd quartile
    q3start = end + q1start
    q3end = end + q1end
    if flag:
        q3 = sum(x[q3start:q3end]) / 2.
    else:
        q3 = sum(x[q3start:q3end])
    print(f"The first quartile is {q1}, the third quartile is {q3}, with the median or 2nd quartile being {median}")
    print(f"The interquartile range is {q3 - q1}") #Find the quartiles
def max(x):
    x = sorted(x) #Sorts list from lowest to highest
    return(x[-1]) #Maximum, this takes the last number from the list to find lowest number
def min(x):
    x = sorted(x) #sorts list from lowest to highest
    return(x[0]) #Minimum, this takes the first number in the list to find lowest number
def numsum(x):
    #i copied my previous code to do this
    x = sorted(x) #sorts our list to prevent random entering of numbers
    print(f'The minimum is {x[0]}') #finds our minimum
    print(f'The maximum is {x[-1]}') #finds our maximum
    #finding our quartiles, uses the same code as above
    length = len(x)  #using copies of long data list
    start = (length)//2 
    if length%2:
        start = start
        end = start + 1
        median = sum(x[start:end]) # sum single element list as value
    else:
        start = start - 1
        end = start + 2
        median = sum(x[start:end]) / 2.  # Average middle two elements
    #finds our first quartile
    q1start = start//2
    flag = False
    if start%2:
        q1start = q1start
        q1end = q1start + 1
        q1 = sum(x[q1start:q1end]) # a single element
    else:
        flag = True
        q1start = q1start - 1
        q1end = q1start + 2
        q1 = sum(x[q1start:q1end]) / 2. # Average middle two elements
    #3rd quartile
    q3start = end + q1start
    q3end = end + q1end
    if flag:
        q3 = sum(x[q3start:q3end]) / 2.
    else:
        q3 = sum(x[q3start:q3end])
        #finding our median, same as above
    no = len(x)
    x.sort()
    if no % 2 == 0:
        median1 = x[no // 2]
        median2 = x[no // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = x[no // 2]

    print(f"The median of all these numbers is {str(median)}")
    print(f"The 1st quartile is {q1}")
    print(f"The 3rd quartile is {q3}") #5 Number Summary
#Testing a random smapling function
def randsamp(x, n): #DEPRECATED, see lazy_functions.py for for the function since it is easier to implement there
    pass
#ALL THE NEEDED FUNCTIONS SO FAR
#EXCLUDING RANDOM SAMPLING