''' === Problem Statement ===

Find the 100001st prime number
'''

# We know we only have to check divsors up to the floor function of the root
# of a number

# Additionally, we know that pi(x) = x / ln(x)

# thus, 10001 = x / ln(x), x = 116684. Thus, we know that the upper bound will
# be < 200,000 (approx).

# Additionally, we know that after checking 2, no even numbers need to be
#  checked.

# Thus, we can run a sieve on 1 - 200000

# Here, we'll use the sieve of erastosthenes

from time import time

t = time()

upperBound = 200000

# Our possible primes are odds from 3 to 200,000
possiblePrimes = list(range(3, 200000, 2))

# Go through all of the possible factors of any of those numbers (3 to 447)
for i in range(3, 1000):
    if i in possiblePrimes:
        # Could also do this by looping through all of the multiples of i...
        # probably better
        possiblePrimes = list(filter(lambda x: x % i != 0 or x == i,
                                     possiblePrimes))

print(possiblePrimes[0:100])

print(time() - t)
