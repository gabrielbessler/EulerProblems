''' === Problem Statement ===

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

# First solution
sum = 0
for i in str(2**1000):
    sum += int(i)

# Second solution
sum = reduce(lambda x, y: x+y, [int(i) for i in str(2**1000)])

# Third Solution (from forum) - probably the best one
sum(int(digit) for digit in str(2**1000))
