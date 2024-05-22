def simples():
    capital = float(input("Valor da parcela: "))
    p = 1 + float(input("Porcentagem dos Juros: "))/100
    meses = float(input("Numero de Parcelas: "))
    m = capital*p
    t = m*meses
    return print("Cada parcela será de ", m, ", e o total de juros será ", t, ".")

def composto():
    capital = float(input("Valor da parcela: "))
    p = 1 + float(input("Porcentagem dos Juros: "))/100
    meses = float(input("Numero de Parcelas: "))
    i = 0
    while i < meses:
        parcela = capital*(p**i)
        print("Mês ",i + 1,": ",parcela,";")
        i += 1
    return print("total: ", capital*(p**meses))

tipo = input("Tipo de Juros (s-simples, c-composto): ")
if tipo == "s": print(simples())
elif tipo  == "c": print(composto())
else: print("escolha uma opcao valida")

