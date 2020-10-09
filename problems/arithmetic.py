def main():
	decimal = int(input(),8)
	hexadecimal = hex(decimal)
	hexaString = str(hexadecimal)
	result = hexaString.replace("0x","")
	print(result.upper())

if __name__ == '__main__':
	main()