def main():
    num_case = int(input())

    for i in range(num_case):
        text = input()

        if text.find("Simon says ") == 0:
            print(text.replace("Simon says ", ""))


if __name__ == '__main__':
    main()
