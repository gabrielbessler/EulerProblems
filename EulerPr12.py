''' === Problem Statement ===

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

import math


def divisors(num):
    ''' finds all of the divisors of a given money '''
    # For a given prime factorization N = (n1 ** a)(n2 ** b)(n3 ** c)...
    # The number of divirsors is (a + 1)(b + 1)(c + 1)...

    # First, we try the greedy approach...
    numfactors = 0

    for i in range(1, int((num)**.5)+1):
        if num % i == 0:
            numfactors += 2
    return numfactors


# Triangle Number: i = 10 = 10+9+8+7+...+1 = i(i+1)/2

i = 1
num = 0
while True:
    num += i
    if i % 100 == 0:
        print(num)
    if divisors(num) >= 500:
        print(num)
        break
    i += 1
