def main():
	k= int(input())
	barSize=1

	numBreaks=[]

	while barSize<k:
		numBreaks.append(barSize)
		barSize*=2

	numBreaks.reverse()

	if barSize==k:
		print(barSize,0)
	else:
		sum=0
		cont=0
		while sum != k :
			if sum>k:
				sum-=numBreaks[cont]
				cont+=1
			else:
				sum+=numBreaks[cont]
				cont+=1
		print(barSize,cont)

if __name__ == '__main__':
	main()