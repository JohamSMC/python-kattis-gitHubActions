def main():
	ouput=0
	for x in range(int(input())):
		aux=input()
		ouput += int(aux[0:-1])**(int(aux[-1]))

	print(ouput)

if __name__ == '__main__':
	main()
