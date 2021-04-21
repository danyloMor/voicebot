n=100#можна любе число через консоль
lst=[i for i in range(1,n+1)]
a=0
s1=0
while a!=(len(lst)):
    for i in lst:
        s1+=lst[a]
        lst[a]=lst[a]**2
        a+=1
s1=s1**2
s=sum(lst)
if s1>s:
    print(s1-s)
else:
    print(s-s1)