def main():
	numCase=int(input())

	for element in range(numCase):
		input()
		Mg ,Mm = map(int,input().split())
		Lg=map(int,input().split())
		Lm=map(int,input().split())

		if max(Lg)>=max(Lm):
			print("Godzilla")
		else:
			print("MechaGodzilla")

if __name__ == '__main__':
	main()