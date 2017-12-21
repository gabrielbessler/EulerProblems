''' === Problem Statement ===

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.
'''

# Maximum we can get is 9! for any given digit
# 9! = 362880
# 99 => 725760
# 999 => 1088640
# 9999 => 1451520
# 99999 => 1814400
# 999999 => 2177280
# 9,999,999 => 2,540,160

# Thus, we know that our upper bound is 7 digits (actually,
# it should be less than 7)

# We want to find the highest 7 digit number we can make that does not
# exceed this value.
# Thus, we start by lowering the 1st digit

# 5,999,999 => 2177400
# 3,999,999 => 2177286
# 2,999,999 => 2177282
# 2,899,999 => 1854722
# Which is too low, so we only have to check numbers from 1 to 3 million

# We're not counting any one digit numbers, so we can start at 10

# For 2 digit numbers, 4 produces 120, so we know that we can only have
# numbers with 3s in BOTH PLACES

# For 3 digit numbers, 7 produces 5040, so we cannot have a 7 in ANY OF THE
# THREE PLACES

# For 4 digit numbers, we cannot have 8 in ANY OF THE FOUR PLACES

# For 5 digit numbers, we cannot have 9 in ANY OF THE FIVE PLACES

from math import factorial
import time

start_time = time.time()
numTotal = 0

for i in range(10, 3000000):
    total = sum([factorial(int(digit)) for digit in str(i)])
    if i == total:
        numTotal += i

    if i % 100000 == 0:
        print(i)

print(numTotal)
print("--- %s seconds ---" % (time.time() - start_time))
