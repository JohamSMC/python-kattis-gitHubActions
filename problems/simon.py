def main():
	numCase=int(input())
	for i in range(numCase):
		text=input()

		if text.find("simon says ")==0:
			print(text.replace("simon says ",""))
		else:
			print("")

if __name__ == '__main__':
	main()