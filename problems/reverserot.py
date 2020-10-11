def main():
	textConvert = input()
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

	while int(textConvert.split(" ")[0]) != 0:
		rotation = int(textConvert.split(" ")[0])
		letters = list(textConvert.split(" ")[1])
		for letter in range(len(letters)):
			indexLetter = alphabet.find(letters[letter])
			newIndexLetter = indexLetter + rotation \
				if (indexLetter + rotation) <= (len(alphabet) - 1) \
				else (indexLetter + rotation) - len(alphabet)
			# print("Letra antigua :",indexLetter,end = "  ")
			# print(letters[letter])
			# print("Letra Nueva :", newIndexLetter, end="  ")
			# print(alphabet[newIndexLetter])
			letters[letter] = alphabet[newIndexLetter]
		letters.reverse()
		output = "".join(letters)
		print(output)

		textConvert = input()

if __name__ == '__main__':
	main()