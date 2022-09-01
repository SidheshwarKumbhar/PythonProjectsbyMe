"""---------------------------------------------------------------------------------------------------
* Mean, Median and Mode are the fundamentals of statistics used in almost every domain where
 we deal with numbers.
* the purpose of the project is to know how to calculate mean, median and mode using Python without
 using any built-in Python library or module.
----------------------------------------------------------------------------------------------------"""
'''
*** Mean ***
The mean is the average value of all the values in a dataset. To calculate the mean value of a dataset,
we first need to find the sum of all the values and then divide the sum of all the values by the
total number of values.'''

dataset = [10, 20, 30, 40, 50, 60]
mean = sum(dataset) / len(dataset)

print("the mean of the data give = ", mean)

'''-------------------------------------------------------------------------------------------------'''
'''
*** Median ***
The Median is the middle value among all the values in sorted order. Here we need to calculate
the mid-value of all the values in a dataset. But before calculating the Median, we need to 
arrange all the values in sorted order.There are two different ways of calculating the median value:

* when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
* when the total number of values is odd: Median = {(n+1)/2}th term '''

# dataset = [10, 20, 30, 40, 50, 60]
dataset.sort()
if len(dataset) % 2 == 0:
    m1 = dataset[len(dataset) // 2]
    m2 = dataset[len(dataset) // 2 + 1]
    median = (m1 + m2) / 2

else:
    median = dataset[len(dataset) // 2]

print('the median of the data set = ', median)

'''--------------------------------------------------------------------------------------------------------'''
'''*** Mode ***
Mode is the most frequently occurring value among all the values.'''

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i

print("the mode of the data set = ", mode)
