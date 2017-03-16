tot = 0
for i in range(1,1001):
  tot += i ** i
  if i % 10 == 0:
      print(i)

print(tot)
