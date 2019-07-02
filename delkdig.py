from itertools import combinations
nsd,n2d=input().split()
n2d=int(n2d)
s=[]
dd=combinations(nsd,len(nsd)-n2d)
for i in list(dd):
  s.append("".join(i))
print(min(s))
