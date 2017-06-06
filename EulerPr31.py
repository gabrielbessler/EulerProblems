'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

import time 

# This is a classic coin problem
# Given a value N 
# How many ways given a set of S coins, can they sum to N?


coins = [1, 2, 5, 10, 20, 50, 100, 200]
goal = 200

''' RECURSIVE APPROACH ''' 

#We do the same calculations over and over again (e.g. recurse(100, L[2:])) would be a subproblem that we do several times 
st = time.time() 
memoDict = {}
def recurse(val = goal, L = coins):
    # We implement the "use it or lose it" approach:
    if (val, tuple(L)) in memoDict:
        #First, we check if this is a value we have already computed
        return memoDict[(val, tuple(L))]
    else: 
        #If not, we can compute it 
        #Base Case
        if val == 0:
            memoDict[(val, tuple(L))] = 1 
        elif val < 0 or len(L) == 0: 
            memoDict[(val, tuple(L))] = 0 
        elif L[0] > val: 
            memoDict[(val, tuple(L))] = 0
        else: 
            useIt = recurse(val - L[0], L)
            loseIt = recurse(val, L[1:]) 
            memoDict[(val, tuple(L))] = useIt + loseIt
        return memoDict[(val, tuple(L))]

print(recurse())
print("Time taken: " + str(time.time() - st))