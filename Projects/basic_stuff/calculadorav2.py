from functools import reduce

def getNumb():
    while True:
        try:
            inp = input("Digite os números a calcular separados por espaço:\n")
            return [int(x) for x in inp.split()]
        except ValueError:
            print('Por favor, digite valores válidos.')
            return getNumb()

def operacao(arr):
    operacoes = {
        'mult':lambda x, y:x*y,
        'div':lambda x, y:x/y,
        'soma':lambda x, y:x+y,
        'sub':lambda x, y:x-y
    }
    op = input('Digite a operação.\n(mult, div, soma, sub):\n')
    if op not in operacoes: 
        print('Digite uma opção válida')
        return operacao(arr)
    r = reduce(operacoes[op], arr)
    return int(r) if r.is_integer() else r

a = operacao(getNumb())
print('Resultado: ', a)