from math import ceil
def main():
	A,I = map(int,input().split())

	aux=A*I
	while ceil(aux/A)>=I:aux-=1 #La funcion ceil()
								#devuelve el valor mas pequeño que no sea X

	print(aux+1)

if __name__ == '__main__':
	main()