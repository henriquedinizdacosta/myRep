a = float(input('n1 - '))
b = float(input('n2 - '))
op = str(input('operação (1: soma; 2: subtração; 3: multiplicação; 4: divisão;) - '))

if op == '1':
    c = a + b
elif op == '2':
    c = a - b
elif op == '3': 
    c = a * b
elif op == '4':
    c = a / b
else: print('digite uma opção valida')

if c.is_integer:
        c = int(c)

print('resultado: ', c)