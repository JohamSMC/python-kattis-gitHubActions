def main():
	R, C, ZR, ZC = input().split(" ")
	rows = []
	for row in range(int(R)):
		rowInput = list(input())
		row = list(map(lambda column : str(column) * int(ZC), rowInput))
		rows.append(''.join(map(str, row)))

	rowsOutput = []
	for row in rows:
		for index in range(int(ZR)):
			rowsOutput.append(row)

	print('\n'.join(map(str, rowsOutput)))

if __name__ == '__main__':
	main()