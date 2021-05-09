def main():
    numbers = input().split()

    print(numbers[0][::-1] if int(numbers[0][::-1]) > int(numbers[1][::-1]) else numbers[1][::-1])


if __name__ == '__main__':
    main()
