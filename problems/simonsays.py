def main():
	numCase=int(input())

	for i in range(numCase):
		text=input()

		if text.find("Simon says ")==0:
			print(text.replace("Simon says ",""))

if __name__ == '__main__':
	main()