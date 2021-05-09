def main():
    k = int(input())
    bar_size = 1

    num_breaks = []

    while bar_size < k:
        num_breaks.append(bar_size)
        bar_size *= 2

    num_breaks.reverse()

    if bar_size == k:
        print(bar_size, 0)
    else:
        sum = 0
        cont = 0
        while sum != k:
            if sum > k:
                sum -= num_breaks[cont]
                cont += 1
            else:
                sum += num_breaks[cont]
                cont += 1
        print(bar_size, cont)


if __name__ == '__main__':
    main()
