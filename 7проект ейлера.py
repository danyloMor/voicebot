import math
N=199999 # діапазон в якому шукаємо прості числа
prime=[x for x in range(N)]
for i in range(2,int(math.ceil(math.sqrt(N)))):  # від 2 до квадратного кореня з N 
        if prime[i]:  # якщо просте видаляємо всі числа кратні до нього
            j=i*i   # для j=2 будуть такі значення 4,6,8,10,12... для j=3 9,12,15,18,21...
            while j<N:
                prime[j]=0
                j+=i
n = []
for i in prime:
    if i not in n:
        n.append(i)
print(n[10000])
