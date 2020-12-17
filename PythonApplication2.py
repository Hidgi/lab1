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
    return a

def enc (g, a, e):
    b_enc = ''
    c = i
    r_enc = len(g) - 1
    a_enc = division(i, g)
    print('c =', a_enc)
    a_enc = '0' * (r_enc - len(a_enc)) + a_enc
    c = c[:-r_enc] + a_enc
    print('a =', c)
    e = '0' * (len(c) - len(e)) + e
    print('e =', e)
    for j in range(len(c)):
        b_enc = b_enc + str((int(c[j]) + int(e[j])) % 2)
    print('b =', b_enc)
    return b_enc

def check(b, g):
    b_check = division(i, g)
    print('При делении ', b, ' на ', g, ' остаток ', b_check)
    if b_check == '' or b_check == '0':
        s = 0
    else:
        s = 1
    return s

def check2(b, g, r):
    a_check = b[:-r]
    a_check = a_check + '0' * (r)
    a_check = division(a, g)
    if a_check == b[-r:]:
        s1 = 0
    else:
        s1 = 1
    return s1

g = input('Введите вектор g(x): ')
k = int(input('Введите k: '))
e = input('Введите e: ')
l = input('Введите l: ')
r = len(g) - 1
m = [0]
a = []
b = []
s = []
s1 = []
if len(l) < k:
    l = '0'*(k-len(l))+l
    m[0] = l
elif len(l) == len(k):
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
    b.append(enc(g, i, e))
for i in b:
     s.append(check(i, g))
     s1.append(check2(i,g,r))
for i in range(len(s)):
    print('Проверка № 1')
    if s[i] == 0:
        print('В ', i + 1, ' части кода ошибок не обнаружено')
    else:
        print('В ', i + 1, ' части кода ошибка обнаружена')
for i in range(len(s)):
    print('Проверка № 2')
    if s1[i] == 0:
        print('В ', i + 1, ' части кода ошибок не обнаружено')
    else:
        print('В ', i + 1, ' части кода ошибка обнаружена')