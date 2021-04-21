a=600851475143
k=[]
for x in range(1,10000):
    for i in range(1,100):
        for l in range(1,100):
            if a%(i*l)!=0 and a%x==0:k.append(x)
print(k[-1])

