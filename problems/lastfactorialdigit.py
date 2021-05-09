def main():
    number_times = int(input())

    for element in range(number_times):
        num = int(input())
        aux = factorial(num)
        print(str(aux)[-1])


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    main()
