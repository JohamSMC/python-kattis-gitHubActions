def main():
	numberTimes=int(input())

	for element in range(numberTimes):
		num=int(input())
		aux=factorial(num)
		print(str(aux)[-1])

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

if __name__ == '__main__':
	main()