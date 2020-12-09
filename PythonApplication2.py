def division(a, g):
    c = a
    while len(a) > r:
        a2 = list(a)
        for i in range(len(g)):
            if a2[i] != g[i]:
                a2[i] = '1'
            else:
                a2[i] = '0'
        a = ''.join(a2)
        while a[0] == '0' and len(a) > 1:
            a = a[1:]
    print('Result of division', c, ' by ', g, ' is ', a)
    return a

g = input('Введите вектор g(x): ')
k = int(input('Введите k: '))
e = input('Введите e: ')
l = input('Введите l: ')
r = len(g) - 1
m = [0]
a = []
b = []
s = []
if len(l) <= k:
    m[0] = l
else:
    m[0] = l[:k]
    l = l[k:]
    while len(l) > k:
        m.append(l[:k])
        l = l[k:]
    m.append(l)
kks = '0' * r
for i in m:
    a.append(i + kks)
for i in a:
    b_enc = ''
    c = i
    r_enc = len(g) - 1
    a_enc = division(i, g)
    a_enc = '0' * (r_enc - len(a_enc)) + a_enc
    c = c[:-r_enc] + a_enc
    e = '0' * (len(c) - len(e)) + e
    for j in range(len(c)):
        b_enc = b_enc + str((int(c[j]) + int(e[j])) % 2)
 
        b.append(b_enc)
for i in b:
    b_check = division(i, g)
    if b_check == '' or b_check == '0':
        res = 0
    else:
        res = 1
    s.append(res)
for i in range(len(s)):
    if s[i] == 0:
        print('В ', i + 1, ' части кода ошибок не обнаружено')
    else:
        print('В ', i + 1, ' части кода ошибка обнаружена')