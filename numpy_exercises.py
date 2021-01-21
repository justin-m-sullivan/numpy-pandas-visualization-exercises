## My Numpy Lesson Exercises

# Use the following code for the questions below:
import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
len(a[a < 0])
    #answer: 4 

# 2. How many positive numbers are there?
positive_nums = a[a > 0]
len(positive_nums)
    #answer: 5

# 3. How many even positive numbers are there?
pos_even_nums = positive_nums[positive_nums % 2 == 0]
len(pos_even_nums)
    #answer: 3

#Other solution from demo:
even_positive_numbers = a[(a > 0) & (a % 2 == 0)]
even_positive_numbers

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
add_three = a + 3
len(add_three[add_three > 0])
    #answer: 10

# 5. If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2

a_squared.mean(), a_sqaured.std()
    #answer: (74.0, 144.0243035046516)

#or
(a ** 2).std()

# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set. 
# See this link for more on centering.
mean_of_a = a.mean()
centered_a = a - mean_of_a
centered_a
    #answer: array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0., -10.])

# 7. Calculate the z-score for each data point.
a_zscore = (a - a.mean()) / a.std()
a_zscore
    #answer: array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
    #   -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
    #   0.        , -1.24034735])

# 8. Copy the setup and exercise directions from 
# More Numpy Practice into your numpy_exercises.py and add your solutions.

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
min_of_a

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
max_of_a

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)
mean_of_a

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
total = 1 
for n in a:
    total *= n
total

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for n in a:
    n = n ** 2
    squares_of_a.append(n)
squares_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [n for n in a if n % 2 != 0]
odds_in_a

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n % 2 == 0]
evens_in_a

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, 
# and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
    ]
b = np.array(b)
b.sum()
b ** 2

# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = b.sum()
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

b.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

b.mean()

# Exercise 5 - refactor the following to use numpy for calculating 
# the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

np.prod(b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

b ** 2
#or
np.power(b, 2)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

b[b % 2 != 0]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
b.shape
    #answer: (2, 3) --> two arrays each with 3 elements

# Exercise 10 - transpose the array b.
b.transpose()
#or
b.T

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape(1,6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6,1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c = np.array(c)

# Exercise 1 - Find the min, max, sum, and product of c.
c.min(), c.max(), c.sum(), c.prod()
    #answer: (1, 9, 45, 362880)

# Exercise 2 - Determine the standard deviation of c.
round(c.std(), 2)
    #answer: 2.58

# Exercise 3 - Determine the variance of c.
round(c.var(), 2)
    #answer: 6.67

# Exercise 4 - Print out the shape of the array c
c.shape
    #answer: (3, 3) --> 3 arrays with 3 elements each

# Exercise 5 - Transpose c and print out transposed result.
print(c.transpose())
[[1 4 7]
[2 5 8]
[3 6 9]]

# Exercise 6 - Get the dot product of the array c with c. 
c.dot(c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sum(sum(c * c.transpose()))




# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.

c = c * c.transpose()
c.prod()

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)

# Exercise 4 - Find all the negative numbers in d
d[d < 0]

array([-90, -30, -45, -45])

# Exercise 5 - Find all the positive numbers in d
d[d > 0]

array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)

array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
    #answer: 11

# Exercise 8 - Print out the shape of d.
d.shape
    #answer: (3, 6)

# Exercise 9 - Transpose and then print out the shape of d.
print(d.transpose())
array([
 [ 90  45  60]
 [ 30 -90  45]
 [ 45 -30 -45]
 [  0 270  90]
 [120  90 -45]
 [180   0 180]
 ])

# Exercise 10 - Reshape d into an array of 9 x 2

d.reshape(9,2)
array([[ 90,  30],
       [ 45,   0],
       [120, 180],
       [ 45, -90],
       [-30, 270],
       [ 90,   0],
       [ 60,  45],
       [-45,  90],
       [-45, 180]])