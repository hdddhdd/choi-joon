n=int(input())
len_n = int(len(str(n)))
ans = 0
for i in range(1, len_n+1):
  if i==len_n:
    ans = ans + i * (n - (10**(i-1)-1))

  else:
    ans = ans + i * 9 * 10**(i-1)
  
print(ans)