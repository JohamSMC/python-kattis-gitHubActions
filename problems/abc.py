def main():
    numbers = list(map(int, input().split()))
    order = input()

    a = min(numbers)
    c = max(numbers)
    numbers.remove(a)
    numbers.remove(c)
    b = numbers[0]

    for i in range(len(order)):
        if order[i] == "A":
            print(a)
        elif order[i] == "B":
            print(b)
        else:
            print(c)


if __name__ == '__main__':
    main()
