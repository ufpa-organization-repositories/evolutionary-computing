def floatToBin(valor):
    f = str(valor)
    inteira, deci = f.split(".")

    print(inteira, deci)
    bint = bin(int(inteira))
    deci = list(deci)
    deci.insert(0,'.')
    print(bint)
    print(deci)

    # inteira
    print('parte inteira')
    if inteira.startswith("-"):
        print('negativo')
        if not len(bint) == 3:
            bint = list(bint[3:])
        else:
            bint = list('0')
        bint.insert(0, "1")
        bint = ''.join(bint)
    else:
        print('positivo')
        if not len(bint) == 2:
        # obs: decimais negativos sao considerados positivos
            bint = list(bint[2:])
        else:
            bint = list('0')
        bint.insert(0, "0")
        bint = ''.join(bint)

    bint = list (bint)
    print(bint, type(bint))

    # decimal
    print('parte decimal')
    multiplicacao = 0
    deci_aux = float(''.join(deci))
    bdeci = []
    while not multiplicacao == 1:
        multiplicacao = (deci_aux * 2)
        a, b = str(multiplicacao).split(".")
        bdeci.append(a)
        # ajuste para decimal
        b = list(b)
        b.insert(0, '.')
        b = str(''.join(b))
        b = float(b)
        deci_aux = b

    print(bdeci, type(bdeci))
    b = bint + bdeci
    print('binario final: ', b)
    return b, [bint, bdeci]

valor = 2.78125
floatToBin(valor)
