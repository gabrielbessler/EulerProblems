'''
Problem 35
the number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

import time

# First, we get a list of all the primes from 1 to 1,000,000

def GetPrimes():
    ''' Inefficient prime algorithm I had already made '''
    upper_bound = 1000000
    #Our possible primes are odds from 3 to 200,000
    possible_primes = [2] + list(range(3,upper_bound,2))
    #Go through all of the possible factors of any of those numbers (3 to 447)
    for i in range(3,1000):
        if i in possible_primes:
            #could also do this by looping through all of the multiples of i...probably better
            possible_primes = list(filter(lambda x: x % i != 0 or x == i, possible_primes))
    return possible_primes

st = time.time()

primes = GetPrimes()

num_circular_primes = 0 

# If the numer is one digit, it only has 1 rotation,  
# e.g. 9 
# If a number has two digits, it has two, 
# e.g. 19 -> 91 
# If a number has three digits, it has three, 
# e.g. 192 -> 219 -> 921
# So for n digits, there are n rotations
# The n'th circle

for i_index, i in enumerate(primes):
    i = str(i)
    if i_index % 1000 == 0: 
        print("Prime Number: " + i)
    circular_prime = True
    for rotation_num in range(len(i)): 
        permutation = i[rotation_num:] + i[:rotation_num] 
        #print(permutation)
        if permutation not in primes: 
            circular_prime = False 
            break
    if circular_prime: 
        num_circular_primes += 1

print(time.time() - st, num_circular_primes)