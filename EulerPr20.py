#Find the sum of the digits in the number 100!

from math import factorial

num = factorial(100)
tot = 0

for i in str(num):
    tot += int(i)

print(tot)


#Alternative solution on forum:
# sum(map(int,str(math.factorial(100))))
