def main():
	numberCases = int(input())

	for x in range(numberCases):
		numberEvaluate = int(input())
		print(str(numberEvaluate)+" is even"
			if numberEvaluate%2 == 0
			else str(numberEvaluate)+" is odd")

if __name__ == '__main__':
	main()