''' === Problem Statement ===

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import time

stime = time.time()

# Would probably be a lot easier to do this using list comprehensions in
# one line.,..
# print(sum(i for i in range(2,5**9)if i==sum(int(j)**5 for j in str(i))))

total = 0
# We are not including 1
for num in range(2, 354294):
    # 7*9**5 is too small to be a seven digit number, so our number must be at
    # most 999,999
    # We find that 6 9's (the maximum value) is only 354,294 (so our number
    # must be smaller than this)
    sum = 0
    for digit in str(num):
        # small optimizations can clearly be made, but this is easier.
        sum += int(digit)**5
    if sum == num:
        total += num
print(total)

print(time.time() - stime)
