''' === Problem Statement ===

 The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
 natural numbers and the square of the sum.
'''

# Solution:

# Note that the sum from 1-100 is (100*101 / 2)**2

sum_squared = (100*101 / 2)**2

# Now note that the formula for the sum of squares is n(n+1)(2n+1) / 6

sum_nums_squared = 100*101*201 / 6

diff = sum_nums_squared - sum_squared

print(diff)

# Runs in O(1)
