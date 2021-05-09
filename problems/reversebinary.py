def main():
    number_evaluate = bin(int(input()))[2:]
    print(int(number_evaluate[::-1], 2))

    # De binario a decimal.

    # b = 11001
    # #Convertimos el entero en una cadena y despeas lo pasamos a binario.
    # #Base 2.
    # print int(str(b), 2)
    # >> > 25

    # De decimal a binario.

    # #Convertimos el entero 25 a binario
    # bin(25)
    # #Nos devuelve una cadena.
    # >> > '0b11001'
    # #Para convertir el numero en un entero.
    # int(bin(25)[2:])


if __name__ == '__main__':
    main()
