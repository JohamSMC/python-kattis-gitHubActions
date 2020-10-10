def main():
	cont=0
	lisNum=[]
	for x in range(5):
		aux=list(map(int,input().split()))
		lisNum.insert(cont,sum(aux))
		cont+=1

	print(lisNum.index(max(lisNum))+1,max(lisNum))

if __name__ == '__main__':
	main()