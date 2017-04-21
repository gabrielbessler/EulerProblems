import math

def divisors(num):
    ''' finds all of the divisors of a given money '''
    # For a given prime factorization N = (n1 ** a)(n2 ** b)(n3 ** c)...
    # The number of divirsors is (a + 1)(b + 1)(c + 1)...

    #First, we try the greedy approach...
    numfactors = 0

    for i in range(1, int((num)**.5)+1):
        if num % i == 0:
            numfactors += 2
    return numfactors


#Triangle Number: i = 10 = 10+9+8+7+...+1 = i(i+1)/2

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
