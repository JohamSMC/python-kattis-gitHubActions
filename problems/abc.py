def main():
	numbers=list(map(int,input().split()))
	order=input()

	A=min(numbers)
	C=max(numbers)
	numbers.remove(A)
	numbers.remove(C)
	B=numbers[0]

	for i in range(len(order)):
		if order[i]=="A":
			print(A)
		elif order[i]=="B":
			print(B)
		else:
			print(C)

if __name__ == '__main__':
	main()