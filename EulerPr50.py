''' === Problem Statement ===

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
 one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime,
 contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most
 consecutive primes?
'''

# First, we use a sieve to get all of the prime numbers up to one million
from time import time
# FIRST IMPLEMENTATION
t = time()
upperBound = 1000000
# Our possible primes are odds from 3 to 200,000
possiblePrimes = list(range(3, upperBound, 2))
# Go through all of the possible factors of any of those numbers (3 to 447)
for i in range(3, int(upperBound ** .5 + 1)):
    if i in possiblePrimes:
        # could also do this by looping through all of the multiples of
        # i...probably better
        possiblePrimes = list(filter(lambda x: x % i != 0 or x == i,
                                     possiblePrimes))
possiblePrimes = [2] + possiblePrimes

total = 0
count = 0
for i in range(len(possiblePrimes)):
    total += possiblePrimes[i]
    count += 1
    if total > 1000000:
        break
print(count)

# our sequence must be at least 22 primes long
# This means our first prime cannot be larger than 45,454
# This also means that we can never sum more than 547

'''
longuestSeqFound = 21
longuestSeqFoundIndex = 0
for i in range(len(possiblePrimes)):
    #we want to find a sum of consecutive primes starting at the current index
    total = sum(possiblePrimes[i:longuestSeqFound+2])
    if total in possiblePrimes:
        longuestSeqFoundIndex = i
        longuestSeqFound += 1
'''

# we know it must be the sum of at least 21 primes equal to at least 1000
# it must also be the sum of either an odd number of primes not containing 2 or
# an even number of primes containing 2
print(time() - t)

''' SECOND IMPLEMENTATION '''
'''
t = time()

#Our possible primes are odds from 3 to 200,000
possiblePrimes = list(range(3,upperBound,2))

currNum = 2
while currNum <= upperBound ** .5:


print(time() - t)
'''