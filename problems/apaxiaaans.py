def main():
	output=input().lower()
	cont=0
	if len(output) == 0:
		print(output)
	else:
		while cont < len(output)-1 :
			if output[cont] == output[cont+1]:
				output=output.replace(output[cont]+output[cont+1],output[cont])
				cont -=1
			cont += 1
		print(output)

if __name__ == '__main__':
	main()