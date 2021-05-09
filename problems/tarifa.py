def main():
    max_month = int(input())

    values_month = []

    number_month = int(input())

    for x in range(number_month):
        values_month.append(int(input()))

    print((max_month*(number_month+1)) - sum(values_month))


if __name__ == '__main__':
    main()
