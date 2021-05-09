from math import ceil


def main():
    a, i = map(int, input().split())

    aux = a*i
    while ceil(aux/a) >= i:
        aux -= 1  # La funcion ceil()
        # devuelve el valor mas pequeño que no sea X

    print(aux+1)


if __name__ == '__main__':
    main()
