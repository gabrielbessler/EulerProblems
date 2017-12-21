''' === Problem Statement ===

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

tot = 0
for i in range(1, 1001):
    tot += i ** i
    if i % 10 == 0:
        print(i)

print(tot)
