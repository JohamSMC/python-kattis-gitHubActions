from typing import List

def main():
	setSize : int = int(input())
	setNumber : int = 1
	while setSize != 0:
		inputData : List[str] = []
		outputData : List[str] = []
		for iteration in range(setSize):
			inputData.append(input())

		#print(inputData)
		outputData = list(filter(lambda x : inputData.index(x) % 2 == 0, inputData))
		outputData += list(filter(lambda x : inputData.index(x) % 2 != 0, inputData))[::-1]

		print("SET "+str(setNumber))
		for data in outputData:
			print(data)
		setSize = int(input())
		setNumber += 1

if __name__ == '__main__':
	main()