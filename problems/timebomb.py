def main():
	numList=["""***
	* *
	* *
	* *
	***""",
	"""  *
	*
	*
	*
	*""",
	"""***
	*
	***
	*  
	***""","""***
	*
	***
	*
	***""","""* *
	* *
	***
	*
	*""","""***
	*  
	***
	*
	***""","""***
	*  
	***
	* *
	***""","""***
	*
	*
	*
	*""","""***
	* *
	***
	* *
	***""","""***
	* *
	***
	*
	***"""]

	line1=input()
	line2=input()
	line3=input()
	line4=input()
	line5=input()

	lenInput=len(line1)
	numNumbers=[7,11,15,19,23,27,31]
			#[2, 3, 4, 5, 6, 7, 8]
	if lenInput==numNumbers[0]: numDigits=2
	if lenInput==numNumbers[1]: numDigits=3
	if lenInput==numNumbers[2]: numDigits=4
	if lenInput==numNumbers[3]: numDigits=5
	if lenInput==numNumbers[4]: numDigits=6
	if lenInput==numNumbers[5]: numDigits=7
	if lenInput==numNumbers[6]: numDigits=8

	invalidDigit=False
	aux=0
	auxOutput=""

	while aux<numDigits and invalidDigit==False:
		invalidDigit = True
		if aux == 0:
			tempNum=line1[0:3] +"\n"+ line2[0:3] +"\n"+ line3[0:3] +"\n"+ line4[0:3] +"\n"+ line5[0:3]
			for x in range(len(numList)):
				if numList[x] == tempNum:
					invalidDigit = False
					auxOutput+=str(x)
		else:
			startChain=4+((aux-1)*4)
			endChain=startChain+3
			tempNum=line1[startChain:endChain]	+"\n"+ line2[startChain:endChain] +"\n"+ line3[startChain:endChain]	+"\n"+line4[startChain:endChain] +"\n"+ line5[startChain:endChain]
			for x in range(len(numList)):
				if numList[x] == tempNum:
					invalidDigit = False
					auxOutput+=str(x)

		aux+=1

	if invalidDigit:
		print("BOOM!!")
	else:
		sumNum=0
		for x in range(len(auxOutput)):
			sumNum+=int(auxOutput[x])
		if int(auxOutput)%2 == 0 and sumNum%3 == 0:
			print("BEER!!")
		else:
			print("BOOM!!")

if __name__ == '__main__':
	main()