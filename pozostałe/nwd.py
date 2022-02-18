def znajdywacz(lista):
    lista.sort()
    lista.reverse()
    poprzednia = 0
    for liczba in lista:
        if liczba == poprzednia:
            return liczba
        poprzednia = liczba
    return 1

def nwd(li1, li2):
    a = []
    b = []
    for i in range(1, li1+1):
        if li1%i == 0:
            a.append(i)
    for i in range(1, li2+1):
        if li2%i == 0:
            b.append(i)
    c = a+b
    return znajdywacz(c)
