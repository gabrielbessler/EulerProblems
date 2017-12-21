''' === Problem Statement ===

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
 each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

# An easy brute force approach would be to first find all of the amicable
# numbers, and then summing them all up.
# The most obvious approach is to go through each number from 1-10000 and see
#  if it has an amicable pair. This would require us to check
# 999 number per number, giving us 999,000. Each check would consist of
#  finding all of the divisors of the number we are comparing it with,
# summing the divisors, etc.
# An easier way is to go through 10,000 numbers, finding all of their divisors
#  once, and sum the disivors for each number. Then, the ones that
# have matches in the list are amicable numbers.
# Yet another way to look at it is to loop through all of the combinations of
# divisors. For example, for a total of 1, we can only have the number 1.
# For a total of 2, nothing exists. For a total of 3, we could have 2*1. For
#  total of 4, we could have 3*1 and 2*2. Etc.... (This one may be more
# mathematically involved)

# METHOD TWO:

divisorsSumL = []
for i in range(1, 10000):

    disivorsSumL.append(divisorsSum)
