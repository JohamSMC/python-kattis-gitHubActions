def main():
	changes= input()
	output=1

	for x in range(len(changes)):
		if output == 1 and changes[x] == 'A':
			output = 2
		elif output == 2 and changes[x] == 'A':
			output = 1
		elif output == 2 and changes[x] == 'B':
			output = 3
		elif output == 3 and changes[x] == 'B':
			output = 2
		elif output == 3 and changes[x] == 'C':
			output = 1
		elif output == 1 and changes[x] == 'C':
			output = 3
	print(output)

if __name__ == '__main__':
	main()