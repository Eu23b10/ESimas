print('divisao de polinomios do 2 grau por um binomio!!!!!!!')

#Divisor dados
g3 = float(input('çççççç: '))
g2 = int(input('termo 2 grau do D: '))
g1 = int(input('termo 1 grau do D: '))
i = int(input('termo independente do D: '))

#dividendo
b = int(input('d - x e igual a: '))

r1 = b*g3
r2 = r1+g2
r3 = r2*b
r4 = r3+g1
r5 = r4*b
r6 = r5+i

print(f'{b} {r1}')
print(F'divisor x+{-b}')
print(f'quociente: {r2}X + {r3}+ {r4}')
print(F'resto: {r4}    {r6}')