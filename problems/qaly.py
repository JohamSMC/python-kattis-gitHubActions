def main():
    number_times = int(input())
    sum = 0.0
    for x in range(number_times):
        numbers = input().split(" ")
        sum += float(numbers[0])*float(numbers[1])
    print("{0:.3f}".format(sum))


if __name__ == '__main__':
    main()
