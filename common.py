last=int(input())
b=[]
for i in range(0,last):
    input1=input()
    b.append(input1)
lai=[]
for i in zip(*b):
    if(i.count(i[0])==len(i)):
        lai.append(i[0])
            
    else:
        break
print(''.join(lai))
