import math
def main():
	inputChain = input().lower()

	inputChain = inputChain.replace('apa','a')
	inputChain = inputChain.replace('epe','e')
	inputChain = inputChain.replace('ipi','i')
	inputChain = inputChain.replace('opo','o')
	inputChain = inputChain.replace('upu','u')

	print(inputChain)

if __name__ == '__main__':
	main()