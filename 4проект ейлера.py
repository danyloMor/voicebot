sum=0
for x in range(100,999):
    for i in range(100,999):
        p=x*i
        p=str(p)
        if p[0]==p[-1]and p[1]==p[-2] and p[2]==p[-3] and p[3]==p[-4]:
            p=int(p)
            if p>sum: 
                sum=p
print(sum)


