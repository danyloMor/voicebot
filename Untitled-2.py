def sim(i):
    k=[2,3,5]
    if len(k)==10:
        return k
    elif not i%2==0 and not i%3==0 and not i%5==0:
        k.append(i)
    return sim(i+1)
print(sim(6))
