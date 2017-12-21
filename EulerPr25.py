''' === Problem Statement

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

s = 0
s_1 = 1
s_2 = 1
index = 0

while len(str(s)) != 1000:
    s_2 = s_1
    s_1 = s
    s += s_2
    index += 1

print(index)


# use one less variable like this
s = 1
s_1 = 1
count = 2

while len(str(s)) != 1000:
    s, s_1 = s + s_1, s
    count += 1

print(count)
