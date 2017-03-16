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




'''use one less variable like this'''
s = 1
s_1 = 1
count = 2

while len(str(s)) != 1000:
    s, s_1 = s + s_1, s
    count += 1

print(count)
