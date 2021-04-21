k=[]
for x in range(1000000,1000000000,10):
    if x%20==0 and x%19==0 and x%11==0 and x%12==0 and x%13==0 and x%14==0 and x%16==0 and x%17==0 and x%18==0:
        k.append(x)
for i in range(2510,1000000,10):
    if i%20==0 and i%19==0 and i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%16==0 and i%17==0 and i%18==0:
        k.append(i)
k.sort()
print(k[0])