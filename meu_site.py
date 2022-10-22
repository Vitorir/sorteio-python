from random import randint

if __name__ == '__main__':
    sorteados = []
    contador = 0

    while contador < 6:
        numero = randint(1,60)
        if not numero in sorteados:
            sorteados.append(numero)
            contador+= 1

    print(sorteados)