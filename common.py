last=int(input())
f=[]
for i in range(0,last):
    input1=input()
    f.append(input1)
lai=[]
for i in zip(*f):
    if(i.count(i[0])==len(i)):
        lai.append(i[0])
            
    else:
        break
print(''.join(lai))
