def main():
	n, c = list(map(int, input().split(" ")))
	fruitWeight = list(map(int, input().split(" ")))
	output = 0
	auxOutput = []

	for i in range(len(fruitWeight)-1):
		if len(fruitWeight)-i <= output:
			break
		auxOutput = []
		for j in range(i,len(fruitWeight)):
			if sum(auxOutput) == c:
				break
			if (fruitWeight[j]+sum(auxOutput) <= c):
				auxOutput.append(fruitWeight[j])
			# print("J =",j,end = "\t")
		if  len(auxOutput) > output:
			output = len(auxOutput)
	print(output)

if __name__ == '__main__':
	main()