#Finding the largest palindrome that can be made from the prodruct of two three digit numbers 

currAns = 0
for i in range(1, 999):
  for k in range(1,999):
      ans = i*k
      if str(ans) == str(ans)[::-1] and len(str(ans)) >= len(str(currAns)):
        if currAns < ans:
            currAns = ans
print(currAns)
