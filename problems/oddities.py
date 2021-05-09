def main():
    number_cases = int(input())

    for x in range(number_cases):
        number_evaluate = int(input())
        print(str(number_evaluate)+" is even"
              if number_evaluate % 2 == 0
              else str(number_evaluate)+" is odd")


if __name__ == '__main__':
    main()
