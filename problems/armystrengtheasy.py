def main():
    num_case = int(input())

    for element in range(num_case):
        input()
        mg, mm = map(int, input().split())
        lg = map(int, input().split())
        lm = map(int, input().split())

        if max(lg) >= max(lm):
            print("Godzilla")
        else:
            print("MechaGodzilla")


if __name__ == '__main__':
    main()
