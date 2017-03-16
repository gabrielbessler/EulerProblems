#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#We know that C > A, B, therefore, A < 500.

''' Perfect Numbers? '''

from math import sqrt
import time

stime = time.time()

count = 0

for a in range(1,251):
    for b in range(1,500):
        c_squared = a**2 + b**2
        if c_squared == int(c_squared):
            if a + b + sqrt(c_squared) == 1000:
                print(a*b*sqrt(c_squared), a, b, c_squared, sqrt(c_squared))

print(time.time() - stime)
