def main():
    text_convert = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

    while int(text_convert.split(" ")[0]) != 0:
        rotation = int(text_convert.split(" ")[0])
        letters = list(text_convert.split(" ")[1])
        for letter in range(len(letters)):
            index_letter = alphabet.find(letters[letter])
            new_index_letter = index_letter + rotation \
                if (index_letter + rotation) <= (len(alphabet) - 1) \
                else (index_letter + rotation) - len(alphabet)
            # print("Letra antigua :",index_letter,end = "  ")
            # print(letters[letter])
            # print("Letra Nueva :", new_index_letter, end="  ")
            # print(alphabet[new_index_letter])
            letters[letter] = alphabet[new_index_letter]
        letters.reverse()
        output = "".join(letters)
        print(output)

        text_convert = input()


if __name__ == '__main__':
    main()
