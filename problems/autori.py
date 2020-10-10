def main():
	author=input()
	split=author.split("-")

	for element in split:
		print(element[0],end="")

if __name__ == '__main__':
	main()