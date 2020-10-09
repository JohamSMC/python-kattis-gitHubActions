def main():
	numberTimes=int(input())

	for element in range(numberTimes):
		auxNumbs=input().split(" ")
		auxNumbs.reverse()

		auxNumbs.pop()

		averageStudents=average(auxNumbs)
		numStudents=0
		for x in range(len(auxNumbs)):
			if int(auxNumbs[x]) >averageStudents:
				numStudents+=1

		porcentajeStudents= (numStudents*100)/len(auxNumbs)
		"""print(round(porcentajeStudents,3))	"""
		print("{0:.3f}".format(porcentajeStudents),"%",sep="")

def average(numbs):
    sum=0.0
    for i in range(len(numbs)):
        sum=sum+int(numbs[i])

    return sum/len(numbs)

if __name__ == '__main__':
	main()