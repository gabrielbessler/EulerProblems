''' === Problem Statement ===

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
 10 terms. Although it has not been proved yet (Collatz Problem), it is
 thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


import time
startTime = time.time()

highestCount = 0
startingNum = 0
for num in range(1, 1000001):
    if num % 10000 == 0:
        print(num)
    startNum = num
    count = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3*num + 1
        count += 1
    if count > highestCount:
        highestCount = count
        startingNum = startNum

print(highestCount, startingNum)
print(time.time() - startTime)

# Solved in 30 sec (no need to optimize,
# although we could easily use memoization, which should
#  speed it up significantly)
