n=int(input())
for i in range(0, n//2+1):
  if (n-2*i)%5==0:
    ans=(n-2*i)//5+i
    break
  else:
    ans = -1
    continue

print(ans)

  