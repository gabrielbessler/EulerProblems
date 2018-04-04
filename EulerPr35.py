''' === Problem Statement ===

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
 73, 79, and 97.
How many circular primes are there below one million?
'''

# We begin by finding all of the primes below 10 million.

maxVal = 2000000
primeList = list(range(0, maxVal + 1))
primeList[0:2] = [0, 0]

# We only need to check up to the sqrt of the max value
for i in range(2, int(maxVal**.5) + 2):
    # By skipping every 2, our algorithm runs a lot faster

    # Method One
    # if i in primeList:
    # Runtime: 10.19seconds (for 2,000,000)

    # Method Two
    # if primeList[(i-1)//2 != 0]
    # RunTime: 1.41seconds
    if primeList[i]:
        y = i**2
        # Method one - RunTime: 1.41 seconds (using only odds)
        '''
        while y < maxVal:
            if y % 2 != 0:
                primeList[(y-1)//2] = 0
            y += i
        '''
        # Method Two - RunTime: .41seconds
        # We want to go from number i*i to maxVal + 1
        primeList[i*i: maxVal+1: i] = [0] * (len(range(i*i, maxVal+1, i)))


# Optimize this with a lc
L = []
for i in primeList:
    if i != 0:
        L.append(i)

newL = []
for i in L:
    if '2' not in str(i) and '5' not in str(i) and '0' not in str(i) and \
       '4' not in str(i) and '6' not in str(i) and '8' not in str(i):
        newL.append(i)
print(len(newL))
# Remember to add 2 for [2] and [5]
