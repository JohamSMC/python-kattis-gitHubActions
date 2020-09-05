def main():
	numberTimes=int(input())
	sum=0.0
	for x in range(numberTimes):
		numbers=input().split(" ")
		sum+=float(numbers[0])*float(numbers[1])
	print("{0:.3f}".format(sum))

if __name__ == '__main__':
	main()
