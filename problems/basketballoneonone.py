def main():
	inputGame = input()
	scoreA = 0
	scoreB = 0
	winA = False
	winB = False
	move = 0

	while (move <= (len(inputGame)-2)):
		if inputGame[move+0] == "A":
			scoreA += 1 if inputGame[move+1] == "1" else 2
		elif inputGame[move+0] == "B":
			scoreB += 1 if inputGame[move+1] == "1" else 2

		if scoreA >= 11 and scoreB < 10:
			winA = True
			break
		elif scoreB >= 11 and scoreA < 10:
			winB = True
			break
		elif scoreA >= 10 and scoreB >= 10:
			if scoreA > scoreB and (scoreA-scoreB) >= 2:
				winA = True
				break
			elif scoreB > scoreA and (scoreB-scoreA) >= 2:
				winB = True
				break
		move += 1

	if winA:
		print("A")
	else:
		print("B")

if __name__ == '__main__':
	main()