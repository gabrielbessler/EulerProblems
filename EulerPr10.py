''' === Problem Statement ===

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# We use the sieve or eratosthenes

from math import floor
import psutil

# May not work for high values, as the sieve has inneficient memory usage.
init = psutil.virtual_memory()[2]

maxVal = 1000
L = list(range(2, maxVal+1))
# We only need to check up to root(maxVal), because if there is a factor over
# root(maxVal), there must also be one under root(maxVal)

final = psutil.virtual_memory()[2]

print("memory usage: " + str(final - init))
# 29% of memory with range of entire values

numsToCheck = floor(maxVal**.5) - 1
for i in range(2, floor(maxVal**.5) + 1):
    if i % 50 == 0:
        print(floor(100*(i / maxVal**.5)))

    # If the current number is not prime
    if L != 0:

        # L[i**2] = 0
        # L[i**2 + i] = 0
        # L[i**2 + 2i] = 0...
        # While i**2 + ni < maxVal, so i(i + n) < maxVal,
        # so (i + n) < maxVal / i, and n < (maxVal/i) - i

        for n in range(0, floor((maxVal/i) - i + 1)):
            # We need the -2 because index 0 is n = 2
            L[i**2 + n*i - 2] = 0

# Alternatively, use filterfalse from itertools
L = list(filter(lambda x: x != 0, L))
# print("Your List of Primes is: " + str(L))
print("Their sum is: " + str(sum(L)))
