def main():
    num_case = int(input())
    for i in range(num_case):
        text = input()

        if text.find("simon says ") == 0:
            print(text.replace("simon says ", ""))
        else:
            print("")


if __name__ == '__main__':
    main()
