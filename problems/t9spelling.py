def main():
    number_cases = int(input())

    letters = list(map(chr, range(65, 91)))
    phone_letters = ["2", "22", "222", "3", "33", "333",
                     "4", "44", "444", "5", "55", "555",
                     "6", "66", "666", "7", "77", "777", "7777",
                     "8", "88", "888", "9", "99", "999", "9999"]

    for z in range(number_cases):
        output = ""
        text_input = input().upper()
        for x in range(len(text_input)):
            if text_input[x] == " ":
                if x > 0 and output[-1] == "0":
                    output += " "
                output += "0"
            else:
                for y in range(len(letters)):
                    if letters[y] == text_input[x]:
                        if x > 0 and output[-1] == phone_letters[y][-1]:
                            output += " "
                        output += phone_letters[y]

        print("Case #" + str(z+1) + ": "+output)


if __name__ == '__main__':
    main()
