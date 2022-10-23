M = int(input('Podaj liczbe strumieni ruchu: '))
V = int(input('Podaj pojemnosc wiazki: '))
a = []
t = []
b = []

for i in range(M):
    a.append(float(input('Podaj a'+ format(i) + ': ')))
    t.append(int(input('Podaj t'+ format(i) + ': ')))

def calc_x(V, M, a, t): #funkcja obliczajaca x
    x = [1] * (V + 1)
    for n in range(1,V+1):
        sum = 0 
        for i in range(0, M):
            if n >= t[i]:
                sum += a[i]*t[i]*x[n-t[i]]
        x[n] = (sum/n)
    return x


def calc_P0(x): #funkcja obliczajaca P0
    sum = 0
    for i in x:
        sum += i
    return 1/sum
    
def calc_Pn(x, V, M, a, t): #funkcja obliczajaca Pn
    P = [1] * (V+1)
    P[0] = calc_P0(x)
    for n in range(1,V+1):
        sum = 0 
        for i in range(0, M):
            if n >= t[i]:
                sum += a[i]*t[i]*P[n-t[i]]
        P[n] = sum/n
    return P
    
    
def calc_Bn(P, V, t, i): #funkcja obliczajaca Bn
    sum = 0 
    for n in range(V - t[i] + 1, V+1):
        sum += P[n]
    return sum 

def calc_all(V, t, a, M):
    x = calc_x(V, M, a, t)
    P = calc_Pn(x, V, M, a, t)
    for i in range(M):
        b.append(calc_Bn(P, V, t, i))
    print('Wartosci x wynosza kolejno: ' + format(x))
    print('Wartosci P wynosza kolejno: ' + format(P))
    print('Wartosci b wynosza kolejno: ' + format(b))

calc_all(V, t, a, M)
