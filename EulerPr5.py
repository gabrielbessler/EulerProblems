'''Problem Statement:

Find the lowest number that is divisible by all numbers from 1 - 20
'''

# Numbers 2,3,4,5,6,7,8,9,10 all fit in 11-20 when divided by 2. This means we
# do not have to check divisors 1-10, leaving numbers 11-20.

# Primes in this range are 11, 13, 17, and 19.

# We know that the lower bound is 2520, as it was given that this number was
# the first one divisible by 1-10. Additionally, we know the upper bound is
# 670442572800
# A brute force approach is too inneficient.


# Running from 20 - 1000000: ~ 1 s
# Iterating BACKWARDS from 20 -> 11 for divisors: > 1.5s

# Let's look at rules of divisibility:

# divisible by 2: must be even
# disivible by 10: must end in 0 (overrides 2). Let step = 10. Result = .14 s
# disivible by 20: let step = 20. Result = .07 sec


from time import time

t = time()

upper = 670442572800
for i in range(2520, upper, 20):
    divisible = True
    for div in range(1,20):
        if i % div != 0:
            divisible = False
            break
    if divisible:
        print(i)
        break
    if i % 10000000 == 0:
        # Print out every 10 million
        print(i)

print(time() - t)
# Answer found in 40 seconds. No need for further optimization.
# Should really use euclidean alg
