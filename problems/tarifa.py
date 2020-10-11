def main():
	maxMonth=int(input())

	valuesMonth=[]

	numberMonth=int(input())

	for x in range(numberMonth):
		valuesMonth.append(int(input()))

	print((maxMonth*(numberMonth+1)) - sum(valuesMonth))

if __name__ == '__main__':
	main()