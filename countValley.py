
#counting valleys

N=int(input())
S=input()
L=0
V=0
for s in S:
    if s == 'U':
        L += 1
        if L == 0:
            V += 1
    else:
        L -= 1
        
print(V)
